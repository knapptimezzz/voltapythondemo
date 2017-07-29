# Libraries
import os
import re
import gzip
import json

# Class
class SnSMessenger:

    # Constructor
    def __init__(self, topic=None, start=None, end=None):
        self.topic = topic
        self.start = start
        self.end = end
        self.data = []
        self.archive_start = None
        self.archive_end = None

    # This function is used in conjunction with the search parameters to build up a list of files to read
    def fetchFileList(self, archive_pointer):
        self.archive_start = os.listdir(archive_pointer)

    def processFiles(self):
        # Open a file to process
        with gzip.open('SnsArchive2017/04/30/23/SnsArchiveFirehose-7-2017-04-30-23-03-54-f6c978d5-2428-48c8-9f6e-6d9a5c407048.gz', 'rb') as f:
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
                # Fetch SNS and Topic
                record["Snsmsg"] = item["Sns"]
                record["Topic"] = item["Sns"]["TopicArn"]
                # Add it to data
                self.data.append(record)

    # This function is used to write data to an output file
    def writeToFile(self):
        return True
