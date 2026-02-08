"""
Path Traversal and File Security Vulnerabilities
This code demonstrates path traversal and file handling vulnerabilities that Snyk can detect.
"""

import os


def read_file(filename):
    """
    VULNERABLE: Path traversal vulnerability
    """
    # VULNERABILITY: No validation of file path
    with open(filename, 'r') as f:
        content = f.read()
    return content


def write_log(log_file, message):
    """
    VULNERABLE: Arbitrary file write
    """
    # VULNERABILITY: User-controlled file path
    with open(log_file, 'a') as f:
        f.write(message + '\n')


def download_file(filepath):
    """
    VULNERABLE: Path traversal in file download
    """
    # VULNERABILITY: Direct path construction without validation
    full_path = os.path.join('/var/www/uploads/', filepath)
    with open(full_path, 'rb') as f:
        return f.read()


def delete_file(filename):
    """
    VULNERABLE: Arbitrary file deletion
    """
    # VULNERABILITY: No path validation
    file_path = f"/tmp/{filename}"
    os.remove(file_path)


# Example of SAFE implementation (for comparison)
def read_file_safe(filename):
    """
    SAFE: Path traversal protection
    """
    # SAFE: Validate and sanitize file path
    base_dir = '/var/www/files/'
    
    # Remove any path traversal attempts
    safe_filename = os.path.basename(filename)
    full_path = os.path.join(base_dir, safe_filename)
    
    # Verify the path is still within base directory
    real_path = os.path.realpath(full_path)
    if not real_path.startswith(os.path.realpath(base_dir)):
        raise ValueError("Invalid file path")
    
    with open(real_path, 'r') as f:
        content = f.read()
    return content
