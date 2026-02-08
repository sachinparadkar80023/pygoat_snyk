# PyGoat Snyk

A deliberately vulnerable Python application designed for security testing and vulnerability scanning with Snyk.

## ⚠️ WARNING

**This repository contains intentionally vulnerable code for educational and testing purposes only.**

**DO NOT:**
- Deploy this code to production
- Use this code in any real application
- Store real credentials or sensitive data
- Expose this application to the internet

## Purpose

This repository demonstrates common security vulnerabilities in Python applications that can be detected by security scanning tools like Snyk. It serves as:

- A testing ground for Snyk vulnerability detection
- Educational material for learning about common security vulnerabilities
- A reference for secure coding practices (safe examples included)

## Vulnerability Categories

This repository includes examples of the following vulnerability types:

### 1. SQL Injection (`sql_injection.py`)
- String concatenation in SQL queries
- String formatting in SQL queries
- F-strings in SQL queries
- Safe parameterized query examples

### 2. Command Injection (`command_injection.py`)
- Shell command injection with `subprocess`
- OS command injection with `os.system`
- Command injection with `os.popen`
- Safe subprocess usage examples

### 3. Insecure Deserialization (`insecure_deserialization.py`)
- Unsafe pickle deserialization
- Unsafe YAML loading
- Safe deserialization examples with JSON

### 4. Hardcoded Secrets (`hardcoded_secrets.py`)
- Hardcoded database passwords
- Hardcoded API keys
- Hardcoded AWS credentials
- Hardcoded encryption keys
- Safe environment variable usage examples

### 5. Path Traversal (`path_traversal.py`)
- Unvalidated file path access
- Arbitrary file write vulnerabilities
- Safe path validation examples

### 6. Cross-Site Scripting (XSS) (`xss_vulnerabilities.py`)
- Reflected XSS in Flask
- Template injection vulnerabilities
- Safe HTML escaping examples

### 7. Vulnerable Dependencies (`requirements.txt`)
- Intentionally outdated packages with known vulnerabilities
- Old versions of Flask, Django, and other popular libraries

## Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Snyk CLI (for scanning)

### Installation

```bash
# Clone the repository
git clone https://github.com/sachinparadkar80023/pygoat_snyk.git
cd pygoat_snyk

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (vulnerable versions)
pip install -r requirements.txt
```

### Running the Application

```bash
python app.py
```

## Scanning with Snyk

### Install Snyk CLI

```bash
npm install -g snyk
```

### Authenticate with Snyk

```bash
snyk auth
```

### Scan for Vulnerabilities

#### Scan Dependencies
```bash
snyk test
```

#### Scan Code
```bash
snyk code test
```

#### Monitor the Project
```bash
snyk monitor
```

### Expected Results

When scanning this repository with Snyk, you should find:

- **High/Critical severity** vulnerabilities in dependencies (outdated packages)
- **Code vulnerabilities** including:
  - SQL Injection
  - Command Injection
  - Insecure Deserialization
  - Hardcoded Secrets
  - Path Traversal
  - Cross-Site Scripting (XSS)

## Learning Resources

Each Python file in this repository includes:
- **Vulnerable code examples** - Demonstrating the security issue
- **Code comments** - Explaining why the code is vulnerable
- **Safe code examples** - Showing how to fix the vulnerability

## Security Best Practices

This repository demonstrates what **NOT** to do. For secure Python development:

1. ✅ Use parameterized queries for database operations
2. ✅ Avoid `shell=True` in subprocess calls
3. ✅ Use `yaml.safe_load()` instead of `yaml.load()`
4. ✅ Store secrets in environment variables or secret managers
5. ✅ Validate and sanitize all user input
6. ✅ Escape HTML output to prevent XSS
7. ✅ Keep dependencies up to date
8. ✅ Regularly scan code with security tools like Snyk

## Contributing

This is an educational project. If you'd like to add more vulnerability examples:

1. Fork the repository
2. Create a new branch for your vulnerability example
3. Add well-documented vulnerable and safe code examples
4. Submit a pull request

## License

This project is for educational purposes. Use at your own risk.

## Disclaimer

The code in this repository is intentionally vulnerable and should only be used for:
- Security testing in isolated environments
- Learning about security vulnerabilities
- Testing security scanning tools

**Never use this code in production or expose it to untrusted networks.**

## Contact

For questions or issues, please open an issue on GitHub.