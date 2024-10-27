pipeline {
    agent any

    stages {
        stage('Create hello.txt') {
            steps {
                script {
                    // Create hello.txt file with "hello jenkins" text content
                    writeFile file: 'hello.txt', text: 'hello from github firewall passed'
                }
                
                // Display the contents of the created file
                sh 'cat hello.txt'
            }
        }
    }

    post {
        success {
            echo 'Successfully created hello.txt with content "hello jenkins".'
        }
        failure {
            echo 'Failed to create hello.txt.'
        }
    }
}
