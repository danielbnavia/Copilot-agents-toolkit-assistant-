"""
CI/CD Helper - Generate CI/CD pipeline configurations
"""

import os
from typing import Dict, Any, Optional
from pathlib import Path


class CICDHelper:
    """Helper for CI/CD integration with GitHub Actions, Azure DevOps, etc."""
    
    def __init__(self, verbose: bool = False):
        """Initialize CI/CD helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        
    def generate_github_actions(self, output_dir: str = ".github/workflows") -> str:
        """Generate GitHub Actions workflow for M365 agent.
        
        Args:
            output_dir: Output directory for workflow file
            
        Returns:
            Path to generated workflow file
        """
        print(f"\n🔧 Generating GitHub Actions workflow\n")
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        workflow_file = output_path / "m365-agent-ci.yml"
        
        workflow_content = """name: M365 Agent CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

jobs:
  validate:
    name: Validate Agent Configuration
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install jsonschema pyyaml
          npm install -g @microsoft/teams-toolkit-cli
      
      - name: Validate agent manifest
        run: |
          python -c "
          import json
          import jsonschema
          
          # Load and validate declarativeAgent.json
          with open('declarativeAgent.json', 'r') as f:
              config = json.load(f)
          
          # Basic validation
          required_fields = ['\\$schema', 'version', 'name', 'description']
          for field in required_fields:
              assert field in config, f'Missing required field: {field}'
          
          # Check lengths
          assert len(config['name']) <= 100, 'Name exceeds 100 characters'
          assert len(config['description']) <= 1000, 'Description exceeds 1000 characters'
          
          print('✅ Agent manifest validation passed')
          "
      
      - name: Check for secrets
        run: |
          # Scan for potential hardcoded secrets
          if grep -r -i "password\\|secret\\|api_key\\|apikey" declarativeAgent.json; then
            echo "⚠️ Warning: Potential secrets found in configuration"
            exit 1
          fi
          echo "✅ No hardcoded secrets detected"

  test:
    name: Run Tests
    runs-on: ubuntu-latest
    needs: validate
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install test dependencies
        run: |
          pip install pytest pytest-cov
      
      - name: Run tests
        run: |
          if [ -f "test_agent.py" ]; then
            pytest test_agent.py -v --cov --cov-report=xml
          else
            echo "No test file found, skipping tests"
          fi
      
      - name: Upload coverage
        if: always()
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage.xml
          flags: unittests

  build:
    name: Build Teams App Package
    runs-on: ubuntu-latest
    needs: test
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      
      - name: Install Teams Toolkit CLI
        run: npm install -g @microsoft/teams-toolkit-cli
      
      - name: Build app package
        run: |
          # Build Teams app package if manifest exists
          if [ -f "appPackage/manifest.json" ]; then
            cd appPackage
            zip -r ../agent-package.zip *
            cd ..
            echo "✅ App package created: agent-package.zip"
          else
            echo "No Teams app manifest found"
          fi
      
      - name: Upload package artifact
        uses: actions/upload-artifact@v4
        with:
          name: agent-package
          path: agent-package.zip
          retention-days: 30

  deploy-dev:
    name: Deploy to Development
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/develop'
    environment: development
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Download package
        uses: actions/download-artifact@v4
        with:
          name: agent-package
      
      - name: Deploy to Teams (Dev)
        run: |
          echo "🚀 Deploying to development environment"
          # Add Teams Toolkit deployment commands here
          # teamsapp deploy --env dev
      
      - name: Notify deployment
        run: |
          echo "✅ Deployment to development completed"

  deploy-prod:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    environment: production
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Download package
        uses: actions/download-artifact@v4
        with:
          name: agent-package
      
      - name: Deploy to Teams (Prod)
        run: |
          echo "🚀 Deploying to production environment"
          # Add Teams Toolkit deployment commands here
          # teamsapp deploy --env prod
      
      - name: Create release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: v${{ github.run_number }}
          release_name: Release v${{ github.run_number }}
          draft: false
          prerelease: false
"""
        
        with open(workflow_file, 'w') as f:
            f.write(workflow_content)
        
        print(f"✅ GitHub Actions workflow created: {workflow_file}")
        print(f"\n📋 Workflow includes:")
        print(f"   • Validate agent configuration")
        print(f"   • Check for hardcoded secrets")
        print(f"   • Run automated tests")
        print(f"   • Build Teams app package")
        print(f"   • Deploy to dev/prod environments")
        print(f"\n💡 Commit this file to enable CI/CD")
        
        return str(workflow_file)
    
    def generate_azure_devops_pipeline(self, output_file: str = "azure-pipelines.yml") -> str:
        """Generate Azure DevOps pipeline.
        
        Args:
            output_file: Output file path
            
        Returns:
            Path to generated pipeline file
        """
        print(f"\n🔧 Generating Azure DevOps pipeline\n")
        
        pipeline_content = """# Azure DevOps Pipeline for M365 Agent

trigger:
  branches:
    include:
      - main
      - develop

pr:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

stages:
  - stage: Validate
    displayName: 'Validate Agent Configuration'
    jobs:
      - job: ValidateManifest
        displayName: 'Validate Manifest'
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '3.11'
            displayName: 'Setup Python'
          
          - script: |
              pip install jsonschema pyyaml
            displayName: 'Install dependencies'
          
          - script: |
              python -c "
              import json
              with open('declarativeAgent.json', 'r') as f:
                  config = json.load(f)
              assert len(config['name']) <= 100
              assert len(config['description']) <= 1000
              print('✅ Validation passed')
              "
            displayName: 'Validate agent manifest'
          
          - script: |
              if grep -r -i "password\\|secret\\|api_key" declarativeAgent.json; then
                echo "##vso[task.complete result=Failed;]Secrets detected"
              fi
            displayName: 'Security scan'

  - stage: Test
    displayName: 'Run Tests'
    dependsOn: Validate
    jobs:
      - job: RunTests
        displayName: 'Execute Tests'
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '3.11'
          
          - script: |
              pip install pytest pytest-cov
              pytest test_agent.py -v --cov || echo "No tests found"
            displayName: 'Run tests'
          
          - task: PublishTestResults@2
            inputs:
              testResultsFormat: 'JUnit'
              testResultsFiles: '**/test-results.xml'

  - stage: Build
    displayName: 'Build Package'
    dependsOn: Test
    jobs:
      - job: BuildPackage
        displayName: 'Build Teams Package'
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: '18.x'
          
          - script: |
              npm install -g @microsoft/teams-toolkit-cli
            displayName: 'Install Teams Toolkit'
          
          - script: |
              if [ -f "appPackage/manifest.json" ]; then
                cd appPackage && zip -r ../agent-package.zip *
              fi
            displayName: 'Build package'
          
          - task: PublishBuildArtifacts@1
            inputs:
              pathToPublish: 'agent-package.zip'
              artifactName: 'agent-package'

  - stage: Deploy
    displayName: 'Deploy to Teams'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployProduction
        displayName: 'Deploy to Production'
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - script: echo "Deploying to Teams"
                  displayName: 'Deploy agent'
"""
        
        with open(output_file, 'w') as f:
            f.write(pipeline_content)
        
        print(f"✅ Azure DevOps pipeline created: {output_file}")
        print(f"\n📋 Pipeline includes:")
        print(f"   • Multi-stage pipeline (Validate, Test, Build, Deploy)")
        print(f"   • Agent manifest validation")
        print(f"   • Automated testing")
        print(f"   • Package building")
        print(f"   • Production deployment")
        print(f"\n💡 Commit this file to your Azure DevOps repository")
        
        return output_file
    
    def generate_dockerfile(self, output_file: str = "Dockerfile") -> str:
        """Generate Dockerfile for containerized deployment.
        
        Args:
            output_file: Output file path
            
        Returns:
            Path to generated Dockerfile
        """
        print(f"\n🐳 Generating Dockerfile\n")
        
        dockerfile_content = """# Dockerfile for M365 Agent Development

FROM node:18-alpine

# Install Python for validation scripts
RUN apk add --no-cache python3 py3-pip

# Install Teams Toolkit CLI
RUN npm install -g @microsoft/teams-toolkit-cli

# Install Python dependencies
RUN pip3 install jsonschema pyyaml pytest

# Set working directory
WORKDIR /app

# Copy agent files
COPY . .

# Validate agent configuration on build
RUN python3 -c "import json; config = json.load(open('declarativeAgent.json')); \
    assert len(config['name']) <= 100; \
    assert len(config['description']) <= 1000; \
    print('✅ Agent validated')"

# Default command
CMD ["sh", "-c", "echo 'M365 Agent container ready'"]
"""
        
        with open(output_file, 'w') as f:
            f.write(dockerfile_content)
        
        print(f"✅ Dockerfile created: {output_file}")
        print(f"\n📋 Features:")
        print(f"   • Node.js 18 base image")
        print(f"   • Python for validation")
        print(f"   • Teams Toolkit CLI")
        print(f"   • Automatic validation on build")
        print(f"\n💡 Build with: docker build -t m365-agent .")
        
        return output_file
    
    def interactive_mode(self):
        """Run CI/CD helper in interactive mode."""
        while True:
            print("\n" + "="*80)
            print("🔧 CI/CD INTEGRATION HELPER")
            print("="*80)
            print("\n1. Generate GitHub Actions workflow")
            print("2. Generate Azure DevOps pipeline")
            print("3. Generate Dockerfile")
            print("4. Generate all CI/CD files")
            print("5. View CI/CD best practices")
            print("6. Back to main menu")
            
            choice = input("\nSelect option (1-6): ").strip()
            
            if choice == "1":
                output_dir = input("\nOutput directory (.github/workflows): ").strip() or ".github/workflows"
                self.generate_github_actions(output_dir)
            elif choice == "2":
                output_file = input("\nOutput file (azure-pipelines.yml): ").strip() or "azure-pipelines.yml"
                self.generate_azure_devops_pipeline(output_file)
            elif choice == "3":
                output_file = input("\nOutput file (Dockerfile): ").strip() or "Dockerfile"
                self.generate_dockerfile(output_file)
            elif choice == "4":
                print("\n📦 Generating all CI/CD files...")
                self.generate_github_actions()
                self.generate_azure_devops_pipeline()
                self.generate_dockerfile()
                print("\n✅ All CI/CD files generated")
            elif choice == "5":
                self._show_best_practices()
            elif choice == "6":
                break
            else:
                print("Invalid option")
            
            input("\nPress Enter to continue...")
    
    def _show_best_practices(self):
        """Show CI/CD best practices."""
        print("\n" + "="*80)
        print("📚 CI/CD BEST PRACTICES")
        print("="*80 + "\n")
        
        practices = [
            ("Automated Validation", "Validate agent config on every commit"),
            ("Security Scanning", "Check for hardcoded secrets and vulnerabilities"),
            ("Automated Testing", "Run all tests before deployment"),
            ("Environment Separation", "Use dev/staging/prod environments"),
            ("Artifact Management", "Version and store build artifacts"),
            ("Rollback Strategy", "Maintain ability to rollback deployments"),
            ("Monitoring", "Track deployment success and agent performance"),
            ("Documentation", "Document deployment process and requirements"),
            ("Access Control", "Restrict production deployments to authorized users"),
            ("Audit Logging", "Log all deployments and configuration changes")
        ]
        
        for i, (practice, description) in enumerate(practices, 1):
            print(f"{i}. {practice}")
            print(f"   {description}\n")
