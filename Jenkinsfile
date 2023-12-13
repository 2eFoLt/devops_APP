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
                script
                {
                    echo 'Testing connection'
                }
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
    	sh 'docker logout'     
    }      
}
}
