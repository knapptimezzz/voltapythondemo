from flask import Flask, render_template, request, send_file
import json
import SnSMessenger
import datetime

app = Flask(__name__)

# Generic route for the end user if they just make a call to the system
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/processform", methods=["POST"])
def processform():
    # Fetch the variables from the request
    start = str(request.form.get("startdate"))
    end = str(request.form.get("enddate"))
    topic = str(request.form.get("topic"))

    if start == "":
        start = None
    if end == "":
        end = None
    if topic == "":
        topic = None

    # If we have time
    if start is not None:
        # If the time is just at date (no time)
        if len(start) <= 10:
            results = start.split("/")
            # Create a datetime for it
            start = datetime.datetime(int(results[2]), int(results[0]), int(results[1]), 0, 0, 0)
        # Else we have date and time to deal with
        elif len(start) > 10:
            results = start.split("-")
            results = results[0].split("/") + results[1].split(":")
            # Build a datetime for that
            start = datetime.datetime(int(results[2]), int(results[0]), int(results[1]), int(results[3]), int(results[4]), int(results[5]))
    # Process end time
    if end is not None:
        # If the time is just at date (no time)
        if len(end) <= 10:
            results = start.split("/")
            # Create a datetime for it
            end = datetime.datetime(int(results[2]), int(results[0]), int(results[1]), 0, 0, 0)
        # Else we have date and time to deal with
        elif len(end) > 10:
            results = end.split("-")
            results = results[0].split("/") + results[1].split(":")
            # Build a datetime for that
            end = datetime.datetime(int(results[2]), int(results[0]), int(results[1]), int(results[3]), int(results[4]), int(results[5]))

    # Create and instance of the class
    sns = SnSMessenger.SnSMessenger(topic=topic, start=start, end=end, pointer='SnsArchive2017')
    # Build a list of files
    sns.fetchFileList()
    sns.processFiles()

    return render_template("index.html")

@app.route("/downloadfile")
def downloadfile():
    try:
        return send_file('output.csv', attachment_filename="output.csv")
    except Exception as e:
        pass

# This is the main function that will run this application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, threaded=False)
