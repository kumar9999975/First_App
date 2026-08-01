pipeline {
    agent any

    // Requires: Docker installed on the Jenkins agent, and (if you use the
    // push stage) a Jenkins "Username with password" credential pointing
    // to your Docker Hub / registry account.
    environment {
        IMAGE_NAME     = "kumar9999975/first-app"
        IMAGE_TAG      = "${env.BUILD_NUMBER}"
        CONTAINER_NAME = "first-app"
        APP_PORT       = "5000"
        DOCKERHUB_CRED = "dockerhub-creds"   // ID of the credential you create in Jenkins
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kumar9999975/First_App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Smoke Test') {
            steps {
                script {
                    sh """
                        docker rm -f ${CONTAINER_NAME}-test || true
                        docker run -d --name ${CONTAINER_NAME}-test -p 5055:${APP_PORT} ${IMAGE_NAME}:${IMAGE_TAG}
                        sleep 5
                        curl -sf http://localhost:5055/ | grep -qi 'Login Form'
                    """
                }
            }
            post {
                always {
                    sh "docker rm -f ${CONTAINER_NAME}-test || true"
                }
            }
        }

        stage('Push to Docker Hub') {
            when {
                branch 'main'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CRED}",
                                                   usernameVariable: 'DOCKER_USER',
                                                   passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "\$DOCKER_PASS" | docker login -u "\$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                        docker push ${IMAGE_NAME}:latest
                    """
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} --restart unless-stopped ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }
    }

    post {
        success {
            echo "Build ${IMAGE_TAG} succeeded and ${CONTAINER_NAME} is running on port ${APP_PORT}."
        }
        failure {
            echo "Pipeline failed — check the stage logs above."
        }
        always {
            sh "docker image prune -f || true"
        }
    }
}
