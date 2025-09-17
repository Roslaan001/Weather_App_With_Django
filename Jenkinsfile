pipeline {
    agent any

    stages {
        stage('Login to the docker registry') {
            steps {
                echo 'Logging in to the docker registry..'
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASSWORD'
                }
            }
        }
        stage('Build the docker image') {
            steps {
                echo 'Building the docker image..'
                sh 'docker build -t abdulsomad005/myapp:2.1 .'

            }
        }
        stage('Push the docker image to the registry(dockerhub') {
            steps {
                echo 'Pushing the docker image..'
                sh 'docker push abdulsomad005/myapp:2.1'
            }
        }
    }
}
