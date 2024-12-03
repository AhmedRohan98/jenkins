pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                withEnv(['PATH+DOCKER=/usr/local/bin:/usr/bin']) {
                    sh 'docker --version'
                }
            }
        }
    }
}


// pipeline {
//     agent {
//         docker { 
//             image 'docker:24.0.2' // Use the Docker CLI image
//         }
//     }
//     environment {
//         GITHUB_TOKEN = credentials('githubtoken') // Use the ID of your GitHub token
//     }
//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t my-python-app .'
//             }
//         }
//         stage('Run Docker Container') {
//             steps {
//                 sh 'docker run -d -p 3000:3000 my-python-app'
//             }
//         }
//     }
// }
