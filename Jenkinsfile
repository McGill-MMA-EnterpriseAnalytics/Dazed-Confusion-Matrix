pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Initialize') {
      steps {
        echo 'Starting dev Jenkins build.'
      }
    }

    stage('Build') {
      steps {
        sh '\'.docker/build\''
      }
    }

  }
}