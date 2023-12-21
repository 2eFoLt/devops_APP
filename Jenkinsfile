pipeline {
    agent any
    environment
    {
        registry_db = "2efolt/devops_db:latest"
        registry_app = "2efolt/devops_app:latest"
        DOCKERHUB_CREDENTIALS= credentials('docker')      
    }
    stages
    {
        stage('Git checkout')
        {
            steps
            {
                git branch: 'dev', url: 'https://github.com/2eFoLt/devops_APP/'
            }
        }
        stage('Static testing')
        {
            steps
            {
                echo 'QoC testing'
                sh 'bandit -r webapp -ii -lll'
                echo 'Style testing'
                sh 'flake8 webapp --ignore=E501,E402'
            }
        }
        stage('Pre-build clean-up')
        {
            steps
            {
                sh 'chmod +x startup/stop.sh'
                sh 'sudo ./startup/stop.sh'
                sh 'chmod +x startup/start.sh'
            }
        }
        stage('Build')
        {
            steps
            {
                script
                {
                    echo 'Building database'
                    sh '''
                    pwd
                    cd db/
                    docker build -t $registry_db .
                    '''
                }
                script
                {
                    echo 'Building app'
                    sh '''
                    pwd
                    cd webapp/
                    docker build -t $registry_app .
                    '''
                }
            }
        }
        stage('Test')
        {
            steps
            {
                sh 'sudo ./startup/start.sh'
                sleep(time:20,unit:"SECONDS")
                echo 'Running tests'
                sh 'id && whoami && pwd'
                sh 'docker exec devops_app bash -c "python -m pytest"'
            }
        }
        stage('Deploy')
        {
            steps
            {
                script
                {
                    echo 'Logging in DockerHub'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
                script
                {
                    echo 'Pushing app'
                    sh 'docker push $registry_app'
                }
                script
                {
                    echo 'Pushing db'
                    sh 'docker push $registry_db'
                }
            }
        }
    }
    post{
        always {
        sh 'sudo ./startup/stop.sh'
    	sh 'docker logout'     
    }      
}
}
