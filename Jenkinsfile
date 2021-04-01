pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Initialize') {
      steps {
        echo 'Starting dev Jenkins build.'
      }
    }

    stage('Build') {
      steps {
        sh 'usermod -a -G docker jenkins'
        sh 'docker build -t dzcm:latest  .'
      }
    }

  }
}