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
                    try {
                        // Simulating failure
                        sh "python3 src/main.py"  // This should trigger the error
                    } catch (Exception e) {
                        echo "❌ Test failed!"
                        currentBuild.result = 'FAILURE'
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
                    // You can trigger your email sending or dev-notification logic here
                    // E.g., run a Python script or use the Jenkins email plugin
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
