pipeline {
    agent any

    parameters {
        string(name: 'GIT_COMMIT', defaultValue: '', description: 'Git commit to build')
    }

    environment {
        GITHUB_REPO = "Sarayu-T/devops-assistant"
        FAILED_FILE = "main.py"  // The buggy file
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: "https://github.com/Sarayu-T/dummy-repo-that-fails.git", branch: 'main'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def result = sh(script: "python3 src/main.py", returnStatus: true)
                    if (result != 0) {
                        echo "❌ Test failed with exit code ${result}!"
                        currentBuild.result = 'FAILURE'
                        error("Tests failed. Halting pipeline.")
                    }
                }
            }
        }

        stage('Notify Developers') {
            when {
                expression { currentBuild.result == 'FAILURE' }
            }
            steps {
                script {
                    echo "⚠️ Sending email notifications to developers..."
                    // Add your email logic or webhook here
                }
            }
        }
    }

    post {
        failure {
            echo "🚨 Build failed, notifying developers."
        }
    }
}
