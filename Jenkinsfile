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