pipeline {
    agent {
        docker { image 'docker:24.0.2' } // Use the Docker CLI image
    }
    environment {
        REPO_URL = 'https://github.com/AhmedRohan98/jenkins.git' // Replace with your repo
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                    docker build -t python-app .
                    '''
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                    docker run -d --rm -p 3000:3000 --name python-app-container python-app
                    '''
                }
            }
        }
    }
    post {
        always {
            // Clean up running containers
            sh 'docker stop python-app-container || true'
        }
    }
}
