pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                ls
                ip a
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
