pipeline {
    agent any

    parameters {
        string(name: 'GIT_COMMIT', defaultValue: '', description: 'Git commit to build')
    }

    environment {
        GITHUB_REPO = "Sarayu-T/devops-assistant"
        FAILED_FILE = "main.py"  // Adjust if needed
        FLASK_TRIGGER_URL = "http://localhost:5000/webhook/jenkins"  // 🔁 Replace this
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    def repoUrl = "https://github.com/Sarayu-T/dummy-repo-that-fails.git"
                    def commit = params.GIT_COMMIT?.trim()
                    
                    if (commit) {
                        echo "📌 Cloning specific commit: ${commit}"
                        checkout([$class: 'GitSCM',
                            branches: [[name: commit]],
                            userRemoteConfigs: [[url: repoUrl]]
                        ])
                    } else {
                        echo "🔄 No commit specified, checking out 'main'"
                        git url: repoUrl, branch: 'main'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "🔍 Attempting to run tests..."

                    def result = bat(
                        script: "C:\\Users\\saray\\AppData\\Local\\Programs\\Python\\Python39\\python.exe src\\main.py",
                        returnStatus: true
                    )

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
    }

    post {
    failure {
        script {
            def jsonPayload = '{"build_number":"24","failed_file":"main.py","repo":"Sarayu-T/devops-assistant","commit":""}'
            bat """
                curl -X POST ^
                -H "Content-Type: application/json" ^
                -d "${jsonPayload}" ^
                https://8f20-223-185-130-123.ngrok-free.app/webhook/jenkins
            """
            }
        }
    }
}
