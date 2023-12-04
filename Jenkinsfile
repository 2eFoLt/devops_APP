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
                    docker_image = docker.build(registry + ":$BUILD_NUMBER")
                }
            }
        }
        stage('Test')
        {
            steps
            {
                docker_image.inside {
                    sh 'Image is alive'
                }
            }
        }
    }
}
