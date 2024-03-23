pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        IMAGE_TAG = "yourdockerhubusername/modelflow:${env.BUILD_ID}"
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_TAG .'
            }
        }
        stage('Publish') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: "$DOCKER_CREDENTIALS_ID", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                    sh 'docker push $IMAGE_TAG'
                }
            }
        }
    }
    post {
        success {
            mail to: 'admin@example.com',
                 subject: "Success: Deployment #${env.BUILD_NUMBER}",
                 body: "The deployment of build #${env.BUILD_NUMBER} was successful."
        }
    }
}
