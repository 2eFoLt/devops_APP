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
                    sh 'cd webapp/'
                    sh 'ls'
                    docker_image = docker.build(registry + ":$BUILD_NUMBER", "-f webapp/Dockerfile")
                }
            }
        }
        stage('Test')
        {
            steps
            {
                script {
                    docker_image.inside {
                    sh 'Image is alive'
                    }
                }
            }
        }
    }
}
