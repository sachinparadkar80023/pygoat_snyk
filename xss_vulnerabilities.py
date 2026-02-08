"""
Cross-Site Scripting (XSS) Vulnerabilities
This code demonstrates XSS vulnerabilities that Snyk can detect.
"""

from flask import Flask, request, render_template_string, Markup


app = Flask(__name__)


@app.route('/search')
def search():
    """
    VULNERABLE: Reflected XSS vulnerability
    """
    # VULNERABILITY: User input directly rendered in HTML without escaping
    query = request.args.get('q', '')
    html = f"<h1>Search Results for: {query}</h1>"
    return html


@app.route('/profile')
def profile():
    """
    VULNERABLE: XSS through template rendering
    """
    # VULNERABILITY: Using render_template_string with user input
    username = request.args.get('name', 'Guest')
    template = f"<h1>Welcome {username}!</h1>"
    return render_template_string(template)


@app.route('/comment')
def show_comment():
    """
    VULNERABLE: XSS using Markup without sanitization
    """
    # VULNERABILITY: Marking user input as safe HTML
    comment = request.args.get('text', '')
    safe_comment = Markup(comment)
    return f"<div>{safe_comment}</div>"


def generate_html(user_input):
    """
    VULNERABLE: Dynamic HTML generation with user input
    """
    # VULNERABILITY: String concatenation with user input
    html = "<div class='user-content'>" + user_input + "</div>"
    return html


# Example of SAFE implementation (for comparison)
from markupsafe import escape


@app.route('/safe_search')
def safe_search():
    """
    SAFE: Proper escaping of user input
    """
    query = request.args.get('q', '')
    # SAFE: Escaping user input
    safe_query = escape(query)
    html = f"<h1>Search Results for: {safe_query}</h1>"
    return html
