from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Generic route for the end user if they just make a call to the system
@app.route("/")
def home():
    return render_template("index.html")

# This is the main function that will run this application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, threaded=False)
