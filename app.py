from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Your Wish</title>
    </head>
    <body>
        <h1>Welcome to Your Wish Flask App!</h1>
        <p>Everything is working fine!</p>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run()
