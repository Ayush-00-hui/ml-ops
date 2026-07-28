#method 1

Download and install jenkins

OR

docker run -d \
  --name jen-mvn \
  --user root \
  -p 8081:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/hadoop/workspace/mlflow-homePrice:/workspace/mlflow-homePrice \
  jenkins/jenkins

 
#url
http://0.0.0.0:8081/

#inside container
apt-get update
apt-get install -y python3-pip
apt install python3.13-venv

sudo apt update  
apt-get install -y docker.io



#method2 custom 

docker build -t jenkins-maven-docker .

docker run -d \
  --name jen-mvn \
  --user root \
  -p 8081:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/hadoop/workspace/mlflow-homePrice:/workspace/mlflow-homePrice \
  jenkins-maven-docker








pipeline {

    agent any

    environment {
        IMAGE_NAME = "house-price"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/chandranitu/mlflow-homeprice.git'
            }
        }

        stage('Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                python src/train.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -f docker/Dockerfile -t house-price:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                docker tag house-price:${BUILD_NUMBER} \
                docker.io/<dockerhub-user>/house-price:${BUILD_NUMBER}

                docker push \
                docker.io/<dockerhub-user>/house-price:${BUILD_NUMBER}
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl set image deployment/house-price \
                house-price=docker.io/<dockerhub-user>/house-price:${BUILD_NUMBER}
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                kubectl rollout status deployment/house-price
                '''
            }
        }
    }
}
