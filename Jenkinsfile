pipeline {
    agent any
    
    options {
        timestamps()
        timeout(time: 1, unit: 'HOURS')
    }
    
    environment {
        BUILD_NAME = "MyApp"
        BUILD_VERSION = "1.0"
        BUILD_DIR = "./build"
        DEPLOY_ENV = "staging"
        DEPLOY_SERVER = "localhost"
        DEPLOY_PORT = "8080"
        TEST_DIR = "./test_results"
        REPORTS_DIR = "./reports"
        LOGS_DIR = "./logs"
        CONFIG_FILE = "config.yaml"
    }
    
    stages {
        stage('Preparation') {
            steps {
                echo '=========================================='
                echo 'Stage: Preparation'
                echo '=========================================='
                echo "Build Name: ${BUILD_NAME}"
                echo "Build Version: ${BUILD_VERSION}"
                echo "Deploy Environment: ${DEPLOY_ENV}"
                
                // Create necessary directories
                sh 'mkdir -p ${BUILD_DIR}'
                sh 'mkdir -p ${REPORTS_DIR}'
                sh 'mkdir -p ${LOGS_DIR}'
                echo ' Preparation completed'
            }
        }
        
        stage('Validate Configuration') {
            steps {
                echo '=========================================='
                echo 'Stage: Validating Configuration'
                echo '=========================================='
                sh 'python config_manager.py --config ${CONFIG_FILE} --env ${DEPLOY_ENV} --action validate'
                echo ' Configuration validation passed'
            }
        }
        
        stage('Build Application') {
            steps {
                echo '=========================================='
                echo 'Stage: Building Application'
                echo '=========================================='
                sh 'python build.py --name ${BUILD_NAME} --ver ${BUILD_VERSION} --dir ${BUILD_DIR}'
                echo ' Build completed successfully'
            }
        }
        
        stage('Generate Build Report') {
            steps {
                echo '=========================================='
                echo 'Stage: Generating Build Report'
                echo '=========================================='
                sh 'python config_manager.py --config ${CONFIG_FILE} --env ${DEPLOY_ENV} --action report'
                echo ' Build report generated'
            }
        }
        
        stage('Deploy to Staging') {
            steps {
                echo '=========================================='
                echo 'Stage: Deploying to ${DEPLOY_ENV}'
                echo '=========================================='
                sh 'python deploy.py --app ${BUILD_NAME} --env ${DEPLOY_ENV} --server ${DEPLOY_SERVER} --port ${DEPLOY_PORT}'
                echo ' Deployment completed'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '=========================================='
                echo 'Stage: Running Tests'
                echo '=========================================='
                sh 'python aggregation.py --test-dir ${TEST_DIR} --output ${REPORTS_DIR} --format detailed'
                echo ' Tests completed'
            }
        }
        
        stage('Process Deployment Logs') {
            steps {
                echo '=========================================='
                echo 'Stage: Processing Deployment Logs'
                echo '=========================================='
                // Create a test log file for processing
                sh '''
                    echo "2025-11-30 10:00:00 - Info - Deployment started" > deployment.log
                    echo "2025-11-30 10:00:05 - Warning - Low disk space detected" >> deployment.log
                    echo "2025-11-30 10:00:10 - Error - Database connection failed" >> deployment.log
                    echo "2025-11-30 10:00:15 - Info - Retrying connection" >> deployment.log
                '''
                sh 'python log_processor.py --logfile deployment.log --output ${LOGS_DIR}'
                echo ' Logs processed'
            }
        }
    }
    
    post {
        always {
            echo '=========================================='
            echo 'Pipeline Execution Summary'
            echo '=========================================='
            echo "Build completed at: ${env.BUILD_TIMESTAMP}"
            echo "Workspace: ${env.WORKSPACE}"
        }
        
        success {
            echo '=========================================='
            echo ' PIPELINE SUCCEEDED!'
            echo '=========================================='
            echo 'All stages completed successfully!'
            echo 'Build artifacts available in:'
            echo '  - Build: ${BUILD_DIR}'
            echo '  - Reports: ${REPORTS_DIR}'
            echo '  - Logs: ${LOGS_DIR}'
            echo 'Ready for production deployment!'
        }
        
        failure {
            echo '=========================================='
            echo ' PIPELINE FAILED!'
            echo '=========================================='
            echo 'One or more stages failed.'
            echo 'Check logs above for details.'
            echo 'Fix the issues and retry.'
        }
        
        unstable {
            echo '=========================================='
            echo ' PIPELINE UNSTABLE'
            echo '=========================================='
            echo 'Some tests may have failed.'
            echo 'Review test results before deploying to production.'
        }
    }
}
