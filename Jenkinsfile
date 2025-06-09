pipeline {

    agent {
        	label 'linux-docker-agent' // <- change to your agent's label
    }
    tools {
        allure 'AllureCLI'
    }

    parameters {
        choice(name: 'BROWSER', choices: ['chrome'], description: 'Choose browser')
        booleanParam(name: 'HEADLESS', defaultValue: false, description: 'Headless mode?')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pytest-runner .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh """
                    mkdir -p allure-results
                    docker run --rm \
                        -v $WORKSPACE/allure-results:/app/allure-results \
                        pytest-runner \
                        pytest --browser=${params.BROWSER} ${params.HEADLESS ? "--headless" : ""} \
                        -v --cache-clear --alluredir=/app/allure-results
                """
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}

