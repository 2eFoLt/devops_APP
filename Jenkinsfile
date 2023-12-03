pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                docker version
                sh '''
                ls
                docker info
                docker compose version 
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                docker compose ps
                curl 0.0.0.0:5000
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
            }
        }
    }
}
