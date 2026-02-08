"""
Command Injection Vulnerability Example
This code demonstrates command injection vulnerabilities that Snyk can detect.
"""

import os
import subprocess
import shlex


def execute_ping(host):
    """
    VULNERABLE: Command Injection vulnerability
    User input is directly passed to shell command
    """
    # VULNERABILITY: Using shell=True with user input
    command = f"ping -c 4 {host}"
    result = subprocess.call(command, shell=True)
    return result


def run_system_command(filename):
    """
    VULNERABLE: Command Injection using os.system
    """
    # VULNERABILITY: Direct use of os.system with user input
    os.system(f"cat {filename}")


def execute_user_command(cmd):
    """
    VULNERABLE: Command Injection using os.popen
    """
    # VULNERABILITY: Using os.popen with user input
    output = os.popen(cmd).read()
    return output


def list_directory(path):
    """
    VULNERABLE: Command Injection in subprocess
    """
    # VULNERABILITY: shell=True with unsanitized input
    subprocess.run(f"ls -la {path}", shell=True, check=True)


# Example of SAFE implementation (for comparison)
def execute_ping_safe(host):
    """
    SAFE: Using subprocess without shell=True and with proper validation
    """
    # SAFE: Using list of arguments without shell=True
    try:
        result = subprocess.run(['ping', '-c', '4', host], 
                              capture_output=True, 
                              text=True, 
                              timeout=10)
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Command timed out"
