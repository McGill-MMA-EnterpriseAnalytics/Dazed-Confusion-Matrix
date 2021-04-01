pipeline {
  agent {
    dockerfile {
      filename 'dzcm:latest'
    }

  }
  stages {
    stage('Initialize') {
      steps {
        echo 'Image built - run or push after'
      }
    }

    stage('Run') {
      steps {
        sh '''docker run -d -p 80:80 dzcm:latest
'''
      }
    }

  }
}