# Libraries
import os
import re
import gzip
import json

# Class
class SnSMessenger:

    # Constructor
    def __init__(self, topic, start, end, pointer):
        self.topic = topic
        self.start = start
        self.end = end
        self.data = []
        self.archive_start = None
        self.archive_end = None
        self.files = []
        self.archive_pointer = pointer

    # This function is used in conjunction with the search parameters to build up a list of files to read
    def fetchFileList(self):
        # Fetch records records
        month_dirs = os.listdir(self.archive_pointer)
        for month in month_dirs:

            day_dirs = os.listdir(self.archive_pointer + "/" + month)
            for day in day_dirs:
                hours_dir = os.listdir(self.archive_pointer + "/" + month + "/" + day)
                for hour in hours_dir:
                    files = os.listdir(self.archive_pointer + "/" + month + "/" + day + "/" + hour)
                    for a_file in files:
                        self.files.append(self.archive_pointer + "/" + month + "/" + day + "/" + hour + "/" + a_file)

        #print (self.files)

    # Process a file one at a time (to save on RAM usage)
    def processFiles(self):
        # Loop through all files
        for a_file in self.files:
            # Open a file to process
            with gzip.open(a_file, 'rb') as f:
                # Fetch content from the file
                content = f.readline()
                # Invalid JSON to start with. Add commas to help with valid json format
                results = re.subn(r'}{', r'},{', content)
                # Take the results of the replacements
                content = results[0]
                # Add brackets around the outside of the content
                content = "[" + content + "]"
                # Dump the contents into a JSON format
                content = json.loads(content)

                # Go through the JSON
                for item in content:
                    # Create a new record
                    record = {}
                    # Fetch SNS and Topic for all records
                    if self.topic is None:
                        record["Snsmsg"] = item["Sns"]
                        record["Topic"] = item["Sns"]["TopicArn"]
                        # Add it to data
                        self.data.append(record)
                    elif item["Sns"]["TopicArn"].endswith(self.topic):
                        record["Snsmsg"] = item["Sns"]
                        record["Topic"] = item["Sns"]["TopicArn"]
                        # Add it to data
                        self.data.append(record)
                    else:
                        pass

            # When finished write out to a file
            self.writeToFile()
            # Clear the list (can't take the chance the user will clear it, users :P )
            self.data = []

    # This function is used to write data to an output file
    def writeToFile(self):
        # Open up a file
        fp = open("output.csv", "w+")
        # Write header information
        fp.write("Topic, SnS Message\n")
        # Loop through all the data
        for item in self.data:
            # Write dat data
            fp.write(str(item["Topic"]) + "," + str(item["Snsmsg"]) + "\n")
