# DevOps Automation Suite

A comprehensive collection of Python automation scripts and Jenkins pipeline for build, deployment, testing, and configuration management workflows.

## 📋 Project Overview

This project demonstrates complete DevOps automation covering:
- **Build Automation** - Compile and package applications
- **Deployment Automation** - Deploy to multiple environments (dev, staging, production)
- **Log Processing** - Analyze and categorize deployment logs
- **Configuration Management** - Validate and apply environment configurations
- **Test Result Aggregation** - Collect and report test results from multiple sources

## 🚀 Features

✅ **Automated Build Pipeline** - Compile sources, run tests, generate build artifacts
✅ **Multi-Environment Deployment** - Deploy to dev, staging, and production with health checks
✅ **Log Analysis** - Extract errors, warnings, and generate reports
✅ **Configuration Validation** - Validate YAML configs before deployment
✅ **Test Aggregation** - Combine results from multiple test files and generate reports
✅ **Jenkins Integration** - Complete Jenkinsfile for CI/CD pipeline automation
✅ **Professional Reporting** - Generate detailed reports with timestamps and recommendations

## 📁 Project Structure

```
devops-automation/
├── build.py                 # Build automation script
├── deploy.py                # Deployment automation script
├── log_processor.py         # Log processing and analysis
├── config_manager.py        # Configuration management
├── aggregation.py           # Test result aggregation
├── Jenkinsfile              # Jenkins pipeline definition
├── config.yaml              # Configuration file (dev, staging, production)
├── test_results/            # Test result files
├── build/                   # Build artifacts
├── deployments/             # Deployment logs
├── reports/                 # Generated reports
└── README.md               # This file
```

## 🛠️ Requirements

- **Python 3.7+**
- **Docker** (for Jenkins)
- **Git** (for version control)
- **YAML** (for config files)

Install dependencies:
```bash
pip install pyyaml
```

## 📚 Scripts Overview

### 1. Build Automation (`build.py`)

Automates the build process with validation and testing.

```bash
python build.py --name MyApp --ver 1.0 --dir ./build
```

**Arguments:**
- `--name` (required) - Application name
- `--ver` (required) - Version number
- `--dir` (required) - Build output directory

**Output:**
- Build artifact file with timestamp
- Exit code 0 (success) or 1 (failure)

---

### 2. Deployment Automation (`deploy.py`)

Deploys applications to specified environments with health checks.

```bash
python deploy.py --app MyApp --env staging --server localhost --port 8080
```

**Arguments:**
- `--app` (required) - Application name to deploy
- `--env` (required) - Environment (dev, staging, production)
- `--server` (required) - Server address
- `--port` (required) - Port number

**Output:**
- Deployment log with status
- Health check results
- Exit code 0 (success) or 1 (failure)

---

### 3. Log Processor (`log_processor.py`)

Analyzes deployment logs and categorizes issues.

```bash
python log_processor.py --logfile deployment.log --output ./logs
```

**Arguments:**
- `--logfile` (required) - Path to log file
- `--output` (required) - Output directory for processed logs

**Analyzes:**
- ERROR messages
- WARNING messages
- INFO messages
- DEBUG messages

**Output:**
- Processed log report with categorized messages

---

### 4. Configuration Manager (`config_manager.py`)

Manages and validates environment configurations.

```bash
# Validate configuration
python config_manager.py --config config.yaml --env staging --action validate

# Generate configuration report
python config_manager.py --config config.yaml --env staging --action report

# Apply configuration
python config_manager.py --config config.yaml --env staging --action apply
```

**Arguments:**
- `--config` (required) - Path to YAML config file
- `--env` (required) - Environment (dev, staging, production)
- `--action` (required) - Action (validate, report, apply)

**Actions:**
- `validate` - Check if config is valid
- `report` - Generate configuration report
- `apply` - Apply configuration to environment

---

### 5. Test Aggregation (`aggregation.py`)

Aggregates test results from multiple sources and generates reports.

```bash
python aggregation.py --test-dir test_results --output ./reports --format summary
```

**Arguments:**
- `--test-dir` (required) - Directory containing test result files
- `--output` (required) - Output directory for aggregated reports
- `--format` (required) - Report format (summary or detailed)

**Output:**
- Aggregated test report
- Pass/fail statistics
- Breakdown by test file
- Failed test details with errors

---

## 📋 Configuration File (config.yaml)

Example configuration file structure:

```yaml
dev:
  build_steps:
    - "npm install"
    - "npm build"
  deploy_steps:
    - "docker build"
    - "docker run"
  notifications: true
  port: 3000

staging:
  build_steps:
    - "npm install"
    - "npm build"
    - "npm test"
  deploy_steps:
    - "docker build"
    - "docker push"
    - "kubectl deploy"
  notifications: true
  port: 8080

production:
  build_steps:
    - "npm install"
    - "npm build"
    - "npm test"
  deploy_steps:
    - "docker build"
    - "docker push registry.io/app:latest"
    - "kubectl deploy --replicas=3"
  notifications: true
  port: 443
```

## 🔄 Jenkins Pipeline

The `Jenkinsfile` defines an automated pipeline with these stages:

1. **Preparation** - Set up environment and directories
2. **Validate Configuration** - Check if config is valid
3. **Build Application** - Compile and test code
4. **Generate Build Report** - Document build process
5. **Deploy to Staging** - Deploy to staging environment
6. **Run Tests** - Execute tests and aggregate results
7. **Process Deployment Logs** - Analyze logs for issues

### Run Pipeline with Jenkins

```bash
# Start Jenkins in Docker
docker run -d -p 8080:8080 -p 50000:50000 \
  --name jenkins \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts-jdk17

# Access Jenkins at http://localhost:8080
# Create new Pipeline job
# Link to this repository (Jenkinsfile)
# Click "Build Now"
```

## 🧪 Sample Test Results File

Create `test_results/test_results_module1.txt`:

```
Test: login_test, Status: PASSED, Time: 0.5s
Test: logout_test, Status: FAILED, Time: 1.2s, Error: Timeout
Test: dashboard_test, Status: PASSED, Time: 0.8s
```

Format: `Test: name, Status: PASSED/FAILED, Time: Xs, Error: message`

## 📊 Expected Outputs

### Build Artifact
```
./build/MyApp_build_staging_20251130_013400.txt
```

### Deployment Log
```
./deployments/MyApp_deployment_staging_20251130_013400.txt
```

### Test Report
```
./reports/test_aggregation_report_20251130_013400.txt
```

### Configuration Report
```
./reports/config_report_staging_20251130_013400.txt
```

## 🎯 DevOps Interview Use Cases

This project covers common DevOps interview topics:

1. **CI/CD Pipeline** - Understanding automation workflows
2. **Infrastructure as Code** - Configuration management with YAML
3. **Logging & Monitoring** - Log analysis and processing
4. **Testing in DevOps** - Test result aggregation
5. **Deployment Strategies** - Multi-environment deployments
6. **Error Handling** - Graceful error management and exit codes
7. **Automation Best Practices** - Professional script structure

## 🚦 Exit Codes

All scripts follow standard Unix exit codes:

- `0` - Success
- `1` - Failure

This allows Jenkins and CI/CD systems to know if a step passed or failed.

## 📝 Git Workflow

Clone and run locally:

```bash
git clone https://github.com/salahhegazy/devops-automation.git
cd devops-automation

# Create feature branch
git checkout -b feature/new-feature

# Make changes
git add .
git commit -m "Add new feature"

# Push to GitHub
git push -u origin feature/new-feature

# Create Pull Request on GitHub (for review)
# Merge to main after review
```

## 🤝 Contributing

1. Create a feature branch
2. Make changes
3. Test thoroughly
4. Commit with descriptive messages
5. Push and create Pull Request

## 📞 Support

For questions about DevOps concepts or script usage, refer to:
- Jenkins Documentation: https://www.jenkins.io/doc/
- Docker Documentation: https://docs.docker.com/
- Python Documentation: https://docs.python.org/3/
- Git Documentation: https://git-scm.com/doc

## 📄 License

MIT License - Feel free to use for learning and interviews

## ✨ Author

Created as part of DevOps interview preparation and automation learning.

---

**Last Updated:** November 30, 2025

**Status:** ✅ Complete - Ready for interviews and production deployment
