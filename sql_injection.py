"""
SQL Injection Vulnerability Example
This code demonstrates SQL injection vulnerabilities that Snyk can detect.
"""

import sqlite3


def get_user_by_username(username):
    """
    VULNERABLE: SQL Injection vulnerability
    User input is directly concatenated into SQL query
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: String concatenation in SQL query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result


def get_user_by_id(user_id):
    """
    VULNERABLE: SQL Injection vulnerability using string formatting
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: String formatting in SQL query
    query = "SELECT * FROM users WHERE id = %s" % user_id
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result


def search_users(search_term):
    """
    VULNERABLE: SQL Injection vulnerability using f-strings
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: F-string in SQL query
    query = f"SELECT * FROM users WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return results


# Example of SAFE implementation (for comparison)
def get_user_safe(username):
    """
    SAFE: Using parameterized queries
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SAFE: Using parameterized query
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    result = cursor.fetchone()
    conn.close()
    return result
