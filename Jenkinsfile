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
        sh 'docker build -t dzcmregistry.azurecr.io/dashboard:latest  .'
      }
    }

  }
}