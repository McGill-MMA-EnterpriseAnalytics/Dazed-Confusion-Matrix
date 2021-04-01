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
        sh './develop up -d'
        sh './develop composer install'
      }
    }

    stage('Package') {
      steps {
        sh './docker/build'
      }
    }

  }
}