pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Test') {
            steps {
                sh 'python test_calculator.py'
            }
        }
    }
}
