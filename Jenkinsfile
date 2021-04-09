pipeline {
  agent any
  stages {
    stage('Initialize') {
      steps {
        echo 'Image built - run or push after'
        sh '''sudo fuser -k 80/tcp || true
'''
      }
    }

    stage('Test & Build') {
      steps {
        echo 'Build with Docker and run Pytest'
        sh 'docker build -t dzcm:latest .'
      }
    }

    stage('Run') {
      steps {
        sh 'docker run -d -p 80:80 dzcm:latest'
      }
    }

  }
}