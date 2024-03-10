import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_geek():
    return f"<h1>Hello from {os.environ['TZ']}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
