pipeline {
    agent any
    
    stages {
        stage("Clean Workspace") {
            steps {
                cleanWs()
            }
        }
        stage("Git Checkout") {
            steps {
                git branch: 'main', url: 'https://github.com/linkedinprojects/basic-flask-app.git'
            }
        }

        stage("Build Docker Image") {
            steps {
                sh "docker build -t githublinkedprojects/basic-flask-app:$BUILD_NUMBER ."
            }
        }

        stage("Tag & Push to DockerHub") {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'docker') {
                        // Tag the image with the build number
                        sh "docker tag linkedinprojects/basic-flask-app:latest githublinkedprojects/basic-flask-app:${env.BUILD_NUMBER}"
                        echo "Logging into Docker Hub..."
                        sh "docker push githublinkedprojects/basic-flask-app:${env.BUILD_NUMBER}"
                    }
                }
            }
        }

        stage("Deploy to Container") {
            steps {
                sh 'docker run -d --name basic-flask-app -p 80:80 githublinkedprojects/basic-flask-app:${env.BUILD_NUMBER}'
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
        success {
            echo 'Pipeline completed successfully! Application deployed.'
        }
        failure {
            echo 'Pipeline failed! Check logs for details.'
        }
    }
}
