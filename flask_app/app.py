from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/second-route")

# @app.route("/third-route")

# @app.route("/fourth-route")

# @app.route("/fifth-route")

if __name__ == "__main__":
    app.run(debug=True)
