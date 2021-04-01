pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
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
        sh 'docker run -d -p 80:80 0b30329ce6f0f93f9595dd10d226996ddba222f1'
      }
    }

  }
}