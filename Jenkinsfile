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
        sh 'docker run $(docker images --format "{{.ID}} {{.CreatedAt}}" | sort -rk 2 | awk \'NR==1{print $1}\')'
      }
    }

  }
}