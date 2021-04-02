pipeline {
  agent any
  stages {
    stage('Initialize') {
      steps {
        echo 'Image built - run or push after'
        sh '''sudo fuser -k 8501/tcp || true
'''
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t dzcm:latest .'
      }
    }

    stage('Run') {
      steps {
        sh 'docker run -d -p 8501:8501 dzcm:latest'
      }
    }

  }
}