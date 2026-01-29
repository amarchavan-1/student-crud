pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = "amarchavan1" 
        IMAGE_NAME = "student-crud-app"
        DOCKER_HUB_CREDS = 'docker-hub-creds' 
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${env.BUILD_NUMBER} ."
                    sh "docker tag ${DOCKER_HUB_USER}/${IMAGE_NAME}:${env.BUILD_NUMBER} ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', DOCKER_HUB_CREDS) {
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }
    }
}
