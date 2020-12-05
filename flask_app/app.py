from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/user_input")

# @app.route("/filtered_data")

# @app.route("/visualizations")

# @app.route("/final_schedule")

if __name__ == "__main__":
    app.run(debug=True)
