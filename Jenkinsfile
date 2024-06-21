pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Test') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }
    }
}
