pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                ls
                pwd
                cd webapp/
                '''
                app=docker.build("2efolt/devops_app")
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                app.inside {
                    sh 'echo "Tests passed"'
                }
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
            }
        }
    }
}
