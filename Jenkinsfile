pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = 'flaskmongo'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-flask-mongo-repo.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy Services') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'curl http://localhost:5000/'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/logs/*.log', allowEmptyArchive: true
        }
    }
}

