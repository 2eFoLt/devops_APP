pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                ls
                docker run hello-world
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
