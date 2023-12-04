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
                    pwd
                    echo $WORKPLACE
                    docker build -f $WORKPLACE/webapp/Dockerfile -t $registry .
                    '''
                }
            }
        }
    }
}
