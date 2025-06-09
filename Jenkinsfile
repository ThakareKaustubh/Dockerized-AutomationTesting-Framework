pipeline {
    agent any
    parameters {
        choice(name: 'BROWSER', choices: ['chrome', 'firefox'], description: 'Choose browser')
        choice(name: 'RE_RUN', choices: ['1', '2', '3', '4', '5'], description: 'Choose number of permissible reruns for failed tests')
        choice(name: 'RE_RUN_DELAY', choices: ['1', '2', '3', '4', '5'], description: 'Choose number of permissible reruns delay between reruns')
        booleanParam(name: 'PARALLEL_EXECUTION', defaultValue: false,, description: 'Launch parallel tests')
        booleanParam(name: 'IS_RE_RUNS', defaultValue: false, description: 'Rerun flaky/failed tests')
        booleanParam(name: 'HEADLESS', defaultValue: false, description: 'Run tests in headless mode')
    }
    tools {
        allure 'AllureCLI'
    }
    stages {
        stage('Clean Allure Results') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'rm -rf allure-results/*'
                    } else {
                        bat 'rmdir /s /q allure-results || exit 0'
                        bat 'mkdir allure-results'
                    }
                }
            }
        }
        stage('Set Python Environment') {
            steps {
                script {
                    env.PYTHON = isUnix() ? 'python3' : 'python'
                }
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                        ${PYTHON} -m venv venv
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        '''
                    } else {
                        bat """
                        ${PYTHON} -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        """
                    }
                }
            }
        }
       stage('Run Tests with Allure') {
    steps {
        script {
            def headlessOption = params.HEADLESS ? "--headless" : ""
            def browser = params.BROWSER
            def parallelExecution = params.PARALLEL_EXECUTION ? "-n auto" : ""
            def isReRun = params.IS_RE_RUNS ? "--reruns ${params.RE_RUN} --reruns-delay ${RE_RUN_DELAY}" : ""

            if (isUnix()) {
                sh """
                    source venv/bin/activate
                    pytest --browser=${browser} ${headlessOption} -v --cache-clear --alluredir=allure-results ${parallelExecution} ${isReRun}
                """
            } else {
                bat """
                    call venv\\Scripts\\activate
                    pytest --browser=${browser} ${headlessOption} -v --cache-clear --alluredir=allure-results ${parallelExecution} ${isReRun}
                """
            }
        }
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
