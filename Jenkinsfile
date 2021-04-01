pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t dzcmregistry.azurecr.io/dashboard:latest  .'
      }
    }

    stage('Run') {
      steps {
        sh '''docker run -d -p 80:80 dzcmregistry.azurecr.io/dashboard:latest
'''
      }
    }

  }
  environment {
    dockerfile = 'True'
  }
}