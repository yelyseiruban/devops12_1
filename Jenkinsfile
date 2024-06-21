pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Configure') {
            steps {
                sh 'apt install python3'
            }
        }
        stage('Test') {
            steps {
                sh 'python test_calculator.py'
            }
        }
    }
}
