pipeline {

  environment {
    imagename = "sikordev/flaskapi"
    registryCredential = 'dockerhub-id'
    dockerImage = ''
  }

  agent {
    label 'dockerhost-label'
  }

  stages {
    stage('Build') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }

    stage('Test') {
      steps{
        script {
          dockerImage.inside {
            sh '/bin/true'
          }
        }
      }
    }

    stage('Push') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
             dockerImage.push('latest')
          }
        }
      }
    }
  }
}
