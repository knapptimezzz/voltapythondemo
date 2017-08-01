# Built in Libraries
import os
import re
import gzip
import json
import datetime

# Class
class SnSMessenger:

    # Constructor
    def __init__(self, topic, start, end, pointer):
        self.topic = topic # String
        self.data = [] # List to hold results
        self.files = [] # List to hold file names
        self.archive_pointer = pointer # Pointer to the start of the dir

        # Make sure start is a date time or set it to the beginning of time (epoch)
        if start is not None:
            self.start = start # Datetime object
        else:
            self.start = datetime.datetime(1970, 1, 1, 0, 0, 0)

        # Make sure end is a date time or set it to the now (epoch)
        if end is not None:
            self.end = end # Datetime object
        else:
            self.end = datetime.datetime.utcnow()
            

    # This function is used in conjunction with the search parameters to build up a list of files to read
    def fetchFileList(self):
        # Fetch records have to drill down with loops
        month_dirs = os.listdir(self.archive_pointer)
        for month in month_dirs:
            day_dirs = os.listdir(self.archive_pointer + "/" + month)
            for day in day_dirs:
                hours_dir = os.listdir(self.archive_pointer + "/" + month + "/" + day)
                for hour in hours_dir:
                    files_list = os.listdir(self.archive_pointer + "/" + month + "/" + day + "/" + hour)
                    for a_file in files_list:
                        file_name = self.archive_pointer + "/" + month + "/" + day + "/" + hour + "/" + a_file
                        # Fetch the file info of the file
                        file_info = a_file.split("-")
                        # Create a date time to compare to
                        dt = datetime.datetime(int(file_info[2]), int(file_info[3]), int(file_info[4]), int(file_info[5]), int(file_info[6]), int(file_info[7]))

                        # If the record falls outside of the time search parameters
                        if dt < self.start or dt > self.end:
                            pass
                        else:
                            self.files.append(file_name)

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
        self.files = []


    # This function is used to write data to an output file
    def writeToFile(self):
        # Open up a file
        fp = open("output.csv", "w")
        # Write header information
        fp.write("Topic, SnS Message\n")
        # Loop through all the data
        for item in self.data:
            # Write dat data
            fp.write(str(item["Topic"]) + "," + str(item["Snsmsg"]) + "\n")
