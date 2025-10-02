#!/usr/bin/env python3
"""
Test script to verify the HTML representation of CommandResult works correctly.
This script can be run to see the HTML output that would appear in Jupyter notebooks.
"""

import sys
import os

# Add the jbang module to the path
sys.path.insert(0, os.path.dirname(__file__))

from jbang.jbang import CommandResult

def test_html_representation():
    """Test the HTML representation of CommandResult."""
    
    print("Testing CommandResult HTML representation...")
    print("=" * 50)
    
    # Test successful command result
    print("\n1. Testing successful command result:")
    success_result = CommandResult(
        stdout="Hello, World!\nThis is a test output.\nMultiple lines work great!",
        stderr="",
        exitCode=0
    )
    
    print("HTML Output:")
    print(success_result._repr_html_())
    
    # Test failed command result
    print("\n2. Testing failed command result:")
    failed_result = CommandResult(
        stdout="Some output before error",
        stderr="Error: Command not found\nUsage: command [options]\n  -h, --help    Show help",
        exitCode=1
    )
    
    print("HTML Output:")
    print(failed_result._repr_html_())
    
    # Test regular string representation
    print("\n3. Testing string representation:")
    print(f"Success result: {success_result}")
    print(f"Failed result: {failed_result}")

if __name__ == "__main__":
    test_html_representation()
