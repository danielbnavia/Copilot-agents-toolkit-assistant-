# CLI Tools Guide

## Overview

The M365 Agent Toolkit Assistant includes powerful CLI tools to enhance your development workflow:

1. **🏪 Template Manager** - Browse and import templates from Agent Store
2. **🧪 Test Framework** - Automated testing with scenarios
3. **🔧 CI/CD Helper** - Generate pipeline configurations

These tools help you build, test, and deploy agents faster and more reliably.

---

## 🏪 Template Manager

Browse the Agent Store and import pre-built templates for common scenarios.

### Features

- **Browse Agent Store** - Explore 50+ pre-built agent templates
- **Filter by Category** - Support, Sales, HR, Analytics, Productivity
- **Sort by Popularity** - By downloads, rating, or name
- **Import Templates** - Download and customize templates
- **Local Management** - Track your installed templates

### Usage

#### Interactive Mode

```bash
python assistant.py --mode template-manager
```

Then select from the menu:
1. Browse Agent Store
2. Import template from Store
3. List local templates
4. Browse by category
5. Back to main menu

#### Browse Agent Store

```
🏪 AGENT STORE - Browse Templates

1. Customer Support Agent
   Category: Support | Author: Microsoft
   ⭐ 4.8/5.0 | 📥 15,000 downloads
   AI agent for customer support with ticket management
   Capabilities: WebSearch, MicrosoftGraph
   Template ID: customer-support

2. Sales Assistant
   Category: Sales | Author: Microsoft
   ⭐ 4.6/5.0 | 📥 12,000 downloads
   CRM integration and lead qualification agent
   Capabilities: MicrosoftGraph, OneDriveAndSharePoint
   Template ID: sales-assistant
```

#### Import a Template

```bash
# Import specific template
template import customer-support

# Specify output directory
template import sales-assistant my-sales-agent
```

The template manager creates:
- `declarativeAgent.json` - Agent configuration
- `instructions.txt` - Agent behavior instructions
- `README.md` - Setup and customization guide

### Available Templates

| Template ID | Category | Rating | Downloads |
|------------|----------|--------|-----------|
| customer-support | Support | 4.8 | 15,000 |
| sales-assistant | Sales | 4.6 | 12,000 |
| hr-onboarding | HR | 4.5 | 8,000 |
| data-analyst | Analytics | 4.7 | 10,000 |
| meeting-assistant | Productivity | 4.4 | 7,500 |

### Customizing Imported Templates

After importing:

1. **Review Configuration** - Check `declarativeAgent.json`
2. **Customize Instructions** - Edit `instructions.txt` for your needs
3. **Add Conversation Starters** - Define common user queries
4. **Configure Capabilities** - Enable needed M365 integrations
5. **Test Locally** - Validate before deployment

---

## 🧪 Test Framework

Automated testing framework with comprehensive test scenarios.

### Features

- **Auto-generate Test Suites** - Create tests from agent configuration
- **Configuration Validation** - Schema compliance and field constraints
- **Security Scanning** - Detect hardcoded secrets
- **Scenario Testing** - Common user interaction patterns
- **Test Reports** - HTML reports with results

### Usage

#### Interactive Mode

```bash
python assistant.py --mode test-framework
```

Menu options:
1. Create test suite for agent
2. Run tests
3. Generate test report
4. View test best practices
5. Back to main menu

#### Create Test Suite

```bash
# In interactive mode
Select option: 1
Enter agent directory path: ./my-agent
```

This generates `test_agent.py` with:
- `test_agent_config_valid()` - JSON validation
- `test_required_fields()` - Required field presence
- `test_schema_url()` - Schema URL correctness
- `test_name_length()` - Name ≤ 100 characters
- `test_description_length()` - Description ≤ 1000 characters
- `test_capabilities_configured()` - Valid capabilities
- `test_conversation_starters()` - 1-5 starters with proper format
- `test_instructions_exist()` - Instructions provided
- `test_no_hardcoded_secrets()` - Security check

#### Run Tests

```bash
# Run generated tests
pytest test_agent.py -v

# Run with coverage
pytest test_agent.py -v --cov --cov-report=html
```

Example output:
```
test_agent.py::TestMyAgent::test_agent_config_valid PASSED
test_agent.py::TestMyAgent::test_required_fields PASSED
test_agent.py::TestMyAgent::test_schema_url PASSED
test_agent.py::TestMyAgent::test_name_length PASSED
test_agent.py::TestMyAgent::test_capabilities_configured PASSED
test_agent.py::TestMyAgent::test_no_hardcoded_secrets PASSED

================== 6 passed in 0.12s ==================
```

#### Generate Test Report

Creates HTML report with:
- Test summary (total, passed, failed)
- Individual test results
- Timestamp and metadata

### Test Best Practices

1. **Configuration Validation** - Always validate JSON schema
2. **Field Constraints** - Enforce length limits (name: 100, description: 1000)
3. **Capability Testing** - Verify correct capability configuration
4. **Security Scanning** - Check for secrets before commit
5. **Scenario Testing** - Test real user interactions
6. **Integration Testing** - Test with actual Teams deployment
7. **Regression Testing** - Re-test after changes
8. **Continuous Testing** - Run tests in CI/CD pipeline

---

## 🔧 CI/CD Helper

Generate CI/CD pipeline configurations for automated deployment.

### Features

- **GitHub Actions** - Complete workflow with validation, testing, deployment
- **Azure DevOps** - Multi-stage pipeline configuration
- **Docker Support** - Containerized deployment
- **Environment Management** - Dev, staging, production
- **Security Scanning** - Automated secret detection

### Usage

#### Interactive Mode

```bash
python assistant.py --mode cicd-helper
```

Menu options:
1. Generate GitHub Actions workflow
2. Generate Azure DevOps pipeline
3. Generate Dockerfile
4. Generate all CI/CD files
5. View CI/CD best practices
6. Back to main menu

#### Generate GitHub Actions

Creates `.github/workflows/m365-agent-ci.yml` with:

**Validation Stage:**
- Checkout code
- Setup Node.js and Python
- Validate agent manifest
- Check for hardcoded secrets

**Test Stage:**
- Run pytest tests
- Generate coverage reports
- Upload to Codecov

**Build Stage:**
- Create Teams app package
- Upload artifacts

**Deploy Stage:**
- Deploy to development (develop branch)
- Deploy to production (main branch)

Example workflow:
```yaml
name: M365 Agent CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate manifest
        run: python validate.py
      
  test:
    needs: validate
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: pytest -v
      
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Teams
        run: teamsapp deploy
```

#### Generate Azure DevOps Pipeline

Creates `azure-pipelines.yml` with:
- Multi-stage pipeline (Validate, Test, Build, Deploy)
- Artifact management
- Environment approvals
- Production deployment gates

#### Generate Dockerfile

Creates containerized environment with:
- Node.js 18 runtime
- Python for validation
- Teams Toolkit CLI
- Automatic validation on build

### CI/CD Best Practices

1. **Automated Validation** - Validate on every commit
2. **Security Scanning** - Check for secrets and vulnerabilities
3. **Automated Testing** - Run all tests before deployment
4. **Environment Separation** - Use dev/staging/prod
5. **Artifact Versioning** - Track all build artifacts
6. **Rollback Strategy** - Maintain rollback capability
7. **Monitoring** - Track deployment success
8. **Access Control** - Restrict production access
9. **Audit Logging** - Log all deployments
10. **Documentation** - Document deployment process

---

## Integration Example

Complete workflow using all CLI tools:

### 1. Import Template

```bash
python assistant.py --mode template-manager
# Select: Import template
# Template ID: customer-support
# Output: ./my-support-agent
```

### 2. Create Tests

```bash
python assistant.py --mode test-framework
# Select: Create test suite
# Agent path: ./my-support-agent
# Creates: ./my-support-agent/test_agent.py
```

### 3. Run Tests

```bash
cd my-support-agent
pytest test_agent.py -v
```

### 4. Generate CI/CD

```bash
python assistant.py --mode cicd-helper
# Select: Generate all CI/CD files
# Creates: .github/workflows/m365-agent-ci.yml
#         azure-pipelines.yml
#         Dockerfile
```

### 5. Commit and Deploy

```bash
git add .
git commit -m "Add customer support agent with tests and CI/CD"
git push origin main
# GitHub Actions automatically runs:
# - Validation
# - Tests
# - Build
# - Deploy to production
```

---

## Command Reference

### Template Manager Commands

```bash
# Interactive mode
python assistant.py --mode template-manager

# Within interactive mode:
browse [category]    # Browse templates
import <id> [dir]    # Import template
list                 # List local templates
```

### Test Framework Commands

```bash
# Interactive mode
python assistant.py --mode test-framework

# Run tests directly
pytest test_agent.py -v
pytest test_agent.py --cov
pytest test_agent.py --html=report.html
```

### CI/CD Helper Commands

```bash
# Interactive mode
python assistant.py --mode cicd-helper

# Generated files can be committed directly
git add .github/workflows/m365-agent-ci.yml
git commit -m "Add CI/CD pipeline"
git push
```

---

## Tips and Tricks

### Template Manager

- **Filter by category** for faster discovery
- **Check ratings** before importing
- **Customize instructions** for your organization
- **Track local templates** to avoid duplicates

### Test Framework

- **Run tests often** during development
- **Use coverage reports** to find untested code
- **Add custom scenarios** for your use cases
- **Integrate with CI/CD** for continuous testing

### CI/CD Helper

- **Start with GitHub Actions** for simplicity
- **Use environment secrets** for credentials
- **Enable branch protection** on main
- **Monitor pipeline runs** in dashboard
- **Set up notifications** for failures

---

## Troubleshooting

### Template Import Fails

```bash
# Check network connection
ping github.com

# Verify template ID
python assistant.py --mode template-manager
# Browse available templates
```

### Tests Fail

```bash
# Install pytest
pip install pytest

# Check test file exists
ls test_agent.py

# Run with verbose output
pytest test_agent.py -vv
```

### CI/CD Pipeline Errors

```bash
# Validate workflow syntax
# Use GitHub Actions extension in VS Code

# Check secrets are configured
# GitHub Settings > Secrets and variables > Actions

# Review workflow run logs
# GitHub Actions tab in repository
```

---

## Next Steps

1. **Explore Templates** - Browse Agent Store for inspiration
2. **Build Tests** - Create comprehensive test suites
3. **Setup CI/CD** - Automate your deployment pipeline
4. **Monitor** - Track deployment success and agent performance
5. **Iterate** - Continuously improve based on feedback

For more information, see:
- [Getting Started Guide](getting-started.md)
- [M365 Agents Knowledge Base](m365-agents-knowledge-base.md)
- [Integration Recommendations](integration-recommendations.md)
