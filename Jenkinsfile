pipeline {
    agent any

    stages {
        stage('Login to the docker registry') {
            steps {
                echo 'Logging in to the docker registry..'
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo -n $DOCKER_PASSWORD | docker login -u $DOCKER_USER --password-stdin docker.io'
                }
            }
        }
        stage('Build the docker image') {
            steps {
                echo 'Building the docker image..'
                sh 'docker build -t abdulsomad005/mydjangoapp:2.1 .'

            }
        }
        stage('Push the docker image to the registry(dockerhub)') {
            steps {
                echo 'Pushing the docker image..'
                sh 'docker push abdulsomad005/mydjangoapp:2.1'
            }
        }
        stage ("Logging in to the EC2 instance using SSH") {
            steps {
                script {
                    echo "Sshing into the ec2 instance"
                sshagent (credentials:['ssh-key']) {
                sh '''

                        mkdir -p ~/.ssh
                        chmod 700 ~/.ssh
                       # Securely add host key to known_hosts to prevent MitM warnings and connection failures
                        ssh-keyscan ec2-3-84-155-68.compute-1.amazonaws.com >> ~/.ssh/known_hosts


                        ssh ubuntu@ec2-3-84-155-68.compute-1.amazonaws.com "sudo apt update && sudo apt upgrade -y"

                        mkdir -p /home/ubuntu/mydjangoapp
                        cd /home/ubuntu/mydjangoapp
                        sudo docker pull abdulsomad005/mydjangoapp:2.1
                        sudo docker run -d -p 8000:8000 abdulsomad005/mydjangoapp:2.1
                    '''
                }
                }
            }
        }
    }
}
