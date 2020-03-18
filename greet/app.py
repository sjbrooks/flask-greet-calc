from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Return simple "Welcome" greeting"""

    html = """
        <html>
            <body>
                <h1>welcome</h1>
            </body>
        </html> 
        """

    return html


@app.route('/welcome/home')
def welcome_home():
    """Return simple "welcome home" greeting"""

    html = """
        <html>
            <body>
                <h1>welcome home</h1>
            </body>
        </html> 
        """

    return html


@app.route('/welcome/back')
def welcome_back():
    """Return simple "welcome back" greeting"""

    html = """
        <html>
            <body>
                <h1>welcome back</h1>
            </body>
        </html> 
        """

    return html