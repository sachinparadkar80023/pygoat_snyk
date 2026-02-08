"""
Main application file demonstrating various vulnerabilities
This is the entry point that imports all vulnerability examples
"""

# Import vulnerability modules
try:
    import sql_injection
    sql_injection_loaded = True
except ImportError:
    sql_injection_loaded = False

try:
    import command_injection
    command_injection_loaded = True
except ImportError:
    command_injection_loaded = False

try:
    import insecure_deserialization
    insecure_deserialization_loaded = True
except ImportError:
    insecure_deserialization_loaded = False

try:
    import hardcoded_secrets
    hardcoded_secrets_loaded = True
except ImportError:
    hardcoded_secrets_loaded = False

try:
    import path_traversal
    path_traversal_loaded = True
except ImportError:
    path_traversal_loaded = False

try:
    import xss_vulnerabilities
    xss_vulnerabilities_loaded = True
except ImportError:
    xss_vulnerabilities_loaded = False


def main():
    """
    Main function that demonstrates vulnerable code patterns
    """
    print("PyGoat Snyk - Vulnerable Python Code for Security Testing")
    print("=" * 60)
    print("\nThis repository contains intentionally vulnerable code")
    print("for security testing and demonstration purposes.")
    print("\nVulnerability Categories:")
    print("1. SQL Injection" + (" ✓" if sql_injection_loaded else " (module loaded)"))
    print("2. Command Injection" + (" ✓" if command_injection_loaded else " (module loaded)"))
    print("3. Insecure Deserialization" + (" ✓" if insecure_deserialization_loaded else " (dependencies required)"))
    print("4. Hardcoded Secrets" + (" ✓" if hardcoded_secrets_loaded else " (dependencies required)"))
    print("5. Path Traversal" + (" ✓" if path_traversal_loaded else " (module loaded)"))
    print("6. Cross-Site Scripting (XSS)" + (" ✓" if xss_vulnerabilities_loaded else " (dependencies required)"))
    print("\nNote: Some modules require dependencies from requirements.txt")
    print("Install with: pip install -r requirements.txt")
    print("\nUse Snyk to scan this repository and detect vulnerabilities:")
    print("  snyk test          - Scan dependencies")
    print("  snyk code test     - Scan code for vulnerabilities")
    print("=" * 60)


if __name__ == "__main__":
    main()
