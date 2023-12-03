pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                ls
                docker version
                docker compose version
                docker compose up -d
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
