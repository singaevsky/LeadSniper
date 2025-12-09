#!/usr/bin/env python3
"""
Script to install dependencies and run the main data collection script
"""
import subprocess
import sys
import os

def install_dependencies():
    """Install required Python packages"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def run_main_script():
    """Run the main data collection script"""
    print("Running main data collection script...")
    try:
        subprocess.check_call([sys.executable, "src/main.py"])
        print("Data collection completed!")
    except subprocess.CalledProcessError as e:
        print(f"Error running main script: {e}")
        sys.exit(1)

def main():
    print("Starting Russian Companies CAT Systems Data Collection")
    print("="*60)
    
    # Install dependencies
    install_dependencies()
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Run main script
    run_main_script()
    
    print("="*60)
    print("Process completed. Check data/companies.csv for results.")

if __name__ == "__main__":
    main()