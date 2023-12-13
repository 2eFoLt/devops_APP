pipeline {
    agent any
    environment
    {
        registry_db = "2efolt/devops_app"
        registry_app = "2efolt/devops_db"
        registryCredential = '2efolt_docker'        
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
                    cd ../webapp/
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
                    sh 'curl 0.0.0.0:5000 | grep HTTP'
                }
            }
        }
    }
}
