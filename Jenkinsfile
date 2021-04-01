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
        sh 'docker build -t jenkins_docker .'
      }
    }

  }
}