"""
Hardcoded Secrets and Credentials
This code demonstrates hardcoded secrets that Snyk can detect.
"""

import requests
from cryptography.fernet import Fernet


# VULNERABILITY: Hardcoded database credentials
DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'admin',
    'password': 'SuperSecret123!',  # Hardcoded password
    'database': 'production_db'
}

# VULNERABILITY: Hardcoded API key
API_KEY = 'sk-1234567890abcdefghijklmnopqrstuvwxyz'

# VULNERABILITY: Hardcoded AWS credentials
AWS_ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
AWS_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'

# VULNERABILITY: Hardcoded encryption key
ENCRYPTION_KEY = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='


def connect_to_database():
    """
    VULNERABLE: Uses hardcoded credentials
    """
    # VULNERABILITY: Using hardcoded password
    connection_string = f"mysql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}/{DATABASE_CONFIG['database']}"
    return connection_string


def call_api(endpoint):
    """
    VULNERABLE: Uses hardcoded API key
    """
    # VULNERABILITY: Hardcoded API key in headers
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def encrypt_data(plaintext):
    """
    VULNERABLE: Uses hardcoded encryption key
    """
    # VULNERABILITY: Hardcoded encryption key
    cipher = Fernet(ENCRYPTION_KEY)
    encrypted = cipher.encrypt(plaintext.encode())
    return encrypted


def get_aws_client():
    """
    VULNERABLE: Hardcoded AWS credentials
    """
    # VULNERABILITY: Hardcoded AWS credentials
    config = {
        'aws_access_key_id': AWS_ACCESS_KEY,
        'aws_secret_access_key': AWS_SECRET_KEY,
        'region_name': 'us-east-1'
    }
    return config


# VULNERABILITY: Hardcoded JWT secret
JWT_SECRET = 'my-super-secret-jwt-key-12345'

# VULNERABILITY: Hardcoded GitHub token
GITHUB_TOKEN = 'ghp_1234567890abcdefghijklmnopqrstuvwxyz'

# VULNERABILITY: Hardcoded private key
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyz
-----END RSA PRIVATE KEY-----"""


# Example of SAFE implementation (for comparison)
import os


def connect_to_database_safe():
    """
    SAFE: Uses environment variables for credentials
    """
    connection_string = (
        f"mysql://{os.environ.get('DB_USER')}:"
        f"{os.environ.get('DB_PASSWORD')}@"
        f"{os.environ.get('DB_HOST')}/"
        f"{os.environ.get('DB_NAME')}"
    )
    return connection_string
