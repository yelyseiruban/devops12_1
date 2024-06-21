pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Configure') {
            steps {
                sh 'pip install python==3.9.7'
            }
        }
        stage('Test') {
            steps {
                sh 'python test_calculator.py'
            }
        }
    }
}
