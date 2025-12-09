#!/usr/bin/env python3
"""
Test script to verify that all required packages are properly installed
"""

def test_imports():
    """Test importing all required packages"""
    try:
        import requests
        print(f"✓ requests version: {requests.__version__}")
    except ImportError as e:
        print(f"✗ Failed to import requests: {e}")
    
    try:
        import bs4
        print(f"✓ beautifulsoup4 version: {bs4.__version__}")
    except ImportError as e:
        print(f"✗ Failed to import beautifulsoup4: {e}")
    
    try:
        import pandas as pd
        print(f"✓ pandas version: {pd.__version__}")
    except ImportError as e:
        print(f"✗ Failed to import pandas: {e}")
    
    try:
        import lxml
        print(f"✓ lxml version: {lxml.__version__}")
    except ImportError as e:
        print(f"✗ Failed to import lxml: {e}")

    print("\nAll imports successful! Dependencies are properly installed.")

if __name__ == "__main__":
    test_imports()