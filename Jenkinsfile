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
                   
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDS}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                        sh "docker logout"
                    }
                }
            }
        }
    }
}
