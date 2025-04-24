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
                    echo "🔍 Attempting to run tests..."

                    // Using 'bat' instead of 'sh' for Windows
                    def result = bat(script: "C:\\Users\\saray\\AppData\\Local\\Programs\\Python\\Python39\\python.exe src\\main.py", returnStatus: true)
                    echo "🔁 Exit code: ${result}"

                    if (result != 0) {
                        echo "❌ Test failed!"
                        error("Tests failed. Exiting pipeline.")
                    } else {
                        echo "✅ Test passed!"
                    }
                }
            }
        }

        stage('Notify Developers') {
            when {
                expression { currentBuild.result == 'FAILURE' }
            }
            steps {
                echo "⚠️ Sending email notifications to developers..."
                // Your email notification logic here
            }
        }
    }

    post {
        failure {
            echo "🚨 Build failed, notifying developers."
        }
    }
}
