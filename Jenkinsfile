pipeline {
    agent any
    environment
    {
        registry = "2efolt/devops_app"
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
                    sh '''
                    ls
                    ls webapp/
                    cd webapp/
                    pwd
                    '''
                    sh 'docker build -t $registry .'
                }
            }
        }
    }
}
