pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Configure') {
            steps {
                sh 'sudo apt install python3'
            }
        }
        stage('Test') {
            steps {
                sh 'python test_calculator.py'
            }
        }
    }
}
