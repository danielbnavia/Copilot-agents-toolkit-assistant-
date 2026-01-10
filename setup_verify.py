#!/usr/bin/env python3
"""
Setup verification script for M365 Agent Toolkit Assistant
Verifies all required SDKs and dependencies are installed
"""

import sys
import subprocess
from typing import Tuple, List


class SetupVerifier:
    """Verify setup and dependencies for M365 Assistant."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.success = []
        
    def check_python_version(self) -> bool:
        """Check Python version."""
        print("🔍 Checking Python version...")
        version = sys.version_info
        
        if version.major >= 3 and version.minor >= 8:
            self.success.append(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
            return True
        else:
            self.errors.append(f"❌ Python {version.major}.{version.minor} - Need Python 3.8 or higher")
            return False
            
    def check_package(self, package_name: str, import_name: str = None) -> bool:
        """Check if a Python package is installed.
        
        Args:
            package_name: Package name (for pip)
            import_name: Import name (if different from package name)
            
        Returns:
            True if package is installed
        """
        if import_name is None:
            import_name = package_name.replace('-', '_')
            
        try:
            __import__(import_name)
            return True
        except ImportError:
            return False
            
    def check_microsoft_packages(self) -> bool:
        """Check Microsoft SDK packages."""
        print("\n🔍 Checking Microsoft SDKs...")
        
        packages = [
            # Bot Framework
            ("botbuilder-core", "botbuilder.core"),
            ("botbuilder-schema", "botbuilder.schema"),
            ("botbuilder-dialogs", "botbuilder.dialogs"),
            ("botbuilder-ai", "botbuilder.ai"),
            
            # Microsoft Graph
            ("msgraph-core", "msgraph.core"),
            ("msgraph-sdk", "msgraph"),
            
            # Azure Identity
            ("azure-identity", "azure.identity"),
            
            # MSAL
            ("msal", "msal"),
        ]
        
        all_installed = True
        for package_name, import_name in packages:
            if self.check_package(package_name, import_name):
                self.success.append(f"✅ {package_name} - Installed")
            else:
                self.errors.append(f"❌ {package_name} - Not installed")
                all_installed = False
                
        return all_installed
        
    def check_azure_packages(self) -> bool:
        """Check Azure SDK packages."""
        print("\n🔍 Checking Azure SDKs...")
        
        packages = [
            ("azure-mgmt-resource", "azure.mgmt.resource"),
            ("azure-mgmt-botservice", "azure.mgmt.botservice"),
            ("azure-mgmt-web", "azure.mgmt.web"),
            ("azure-storage-blob", "azure.storage.blob"),
        ]
        
        all_installed = True
        for package_name, import_name in packages:
            if self.check_package(package_name, import_name):
                self.success.append(f"✅ {package_name} - Installed")
            else:
                self.warnings.append(f"⚠️  {package_name} - Not installed (optional for deployment)")
                
        return all_installed
        
    def check_utility_packages(self) -> bool:
        """Check utility packages."""
        print("\n🔍 Checking utility packages...")
        
        packages = [
            ("aiohttp", "aiohttp"),
            ("requests", "requests"),
            ("python-dotenv", "dotenv"),
            ("pyyaml", "yaml"),
            ("jsonschema", "jsonschema"),
            ("rich", "rich"),
        ]
        
        all_installed = True
        for package_name, import_name in packages:
            if self.check_package(package_name, import_name):
                self.success.append(f"✅ {package_name} - Installed")
            else:
                self.errors.append(f"❌ {package_name} - Not installed")
                all_installed = False
                
        return all_installed
        
    def check_node_and_npm(self) -> bool:
        """Check Node.js and npm installation."""
        print("\n🔍 Checking Node.js and npm...")
        
        # Check Node.js
        try:
            result = subprocess.run(
                ["node", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip()
                self.success.append(f"✅ Node.js {version} - Installed")
                node_ok = True
            else:
                self.warnings.append("⚠️  Node.js - Not found (needed for Teams Toolkit)")
                node_ok = False
        except (FileNotFoundError, subprocess.TimeoutExpired):
            self.warnings.append("⚠️  Node.js - Not found (needed for Teams Toolkit)")
            node_ok = False
            
        # Check npm
        try:
            result = subprocess.run(
                ["npm", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip()
                self.success.append(f"✅ npm {version} - Installed")
                npm_ok = True
            else:
                self.warnings.append("⚠️  npm - Not found (needed for Teams Toolkit)")
                npm_ok = False
        except (FileNotFoundError, subprocess.TimeoutExpired):
            self.warnings.append("⚠️  npm - Not found (needed for Teams Toolkit)")
            npm_ok = False
            
        return node_ok and npm_ok
        
    def check_teams_toolkit(self) -> bool:
        """Check Teams Toolkit CLI."""
        print("\n🔍 Checking Teams Toolkit...")
        
        try:
            result = subprocess.run(
                ["teamsfx", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip()
                self.success.append(f"✅ Teams Toolkit CLI {version} - Installed")
                return True
            else:
                self.warnings.append("⚠️  Teams Toolkit CLI - Not found (optional, can install with: npm install -g @microsoft/teamsfx-cli)")
                return False
        except (FileNotFoundError, subprocess.TimeoutExpired):
            self.warnings.append("⚠️  Teams Toolkit CLI - Not found (optional, can install with: npm install -g @microsoft/teamsfx-cli)")
            return False
            
    def print_summary(self):
        """Print verification summary."""
        print("\n" + "="*70)
        print("📊 SETUP VERIFICATION SUMMARY")
        print("="*70)
        
        if self.success:
            print("\n✅ INSTALLED PACKAGES:")
            for item in self.success:
                print(f"  {item}")
                
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for item in self.warnings:
                print(f"  {item}")
                
        if self.errors:
            print("\n❌ ERRORS (REQUIRED PACKAGES MISSING):")
            for item in self.errors:
                print(f"  {item}")
                
        print("\n" + "="*70)
        
        if self.errors:
            print("\n🔧 TO FIX ERRORS:")
            print("   Run: pip install -r requirements.txt")
            print("\n📦 TO INSTALL OPTIONAL PACKAGES:")
            print("   Node.js: https://nodejs.org/")
            print("   Teams Toolkit CLI: npm install -g @microsoft/teamsfx-cli")
            return False
        else:
            print("\n🎉 All required packages are installed!")
            if self.warnings:
                print("   Some optional packages are missing but you can still use the assistant.")
            return True
            
    def run_verification(self) -> bool:
        """Run all verification checks.
        
        Returns:
            True if all required packages are installed
        """
        print("="*70)
        print("🚀 M365 AGENT TOOLKIT ASSISTANT - SETUP VERIFICATION")
        print("="*70)
        
        self.check_python_version()
        self.check_microsoft_packages()
        self.check_azure_packages()
        self.check_utility_packages()
        self.check_node_and_npm()
        self.check_teams_toolkit()
        
        return self.print_summary()


def main():
    """Main entry point."""
    verifier = SetupVerifier()
    success = verifier.run_verification()
    
    if success:
        print("\n✅ You're ready to use the M365 Agent Toolkit Assistant!")
        print("   Run: python assistant.py")
        sys.exit(0)
    else:
        print("\n❌ Please install missing packages before using the assistant.")
        sys.exit(1)


if __name__ == "__main__":
    main()
