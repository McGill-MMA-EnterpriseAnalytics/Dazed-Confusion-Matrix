pipeline {
  agent any
  stages {
    stage('Initialize') {
      steps {
        echo 'Starting dev Jenkins build.'
      }
    }

    stage('Build') {
      steps {
        sh '''docker build -t dzcm:latest  .
'''
      }
    }

  }
}