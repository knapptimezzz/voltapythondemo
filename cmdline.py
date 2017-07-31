# Built in Library
import sys
import datetime

# Custome library imports
import SnSMessenger

# Initialize variables
help_menu = False
start = None
end = None
topic = None

# Parse out the arguments
for i in range(0, len(sys.argv)):
    # Check for help
    if sys.argv[i] == "--help":
        help_menu = True
    # Check for a start time
    if sys.argv[i] == "-s":
        start = sys.argv[i + 1]
    # Check for an end time
    if sys.argv[i] == "-e":
        end = sys.argv[i + 1]
    # Check for a topic
    if sys.argv[i] == "-t":
        topic = sys.argv[i + 1]

# If the user wants help
if help_menu:
    # Show the user the help menu
    print("\nThis is the help menu for the cmdline python application for Volta.")
    print("Options for this application include\n")
    print("   -s\t\t'start time'-the lower limit of time you would like to search from mm/dd/yyyy-hh:mm:ss format")
    print("   -e\t\t'end time'-the upper limit of time you would like to search too mm/dd/yyyy-hh:mm:ss format")
    print("   -t\t\t'topic'-a topic you would like to search for")
    print("   --help\tPresent a help menu for the user. Overrides all other options\n")
    print("If no start time is selected the system will pick the earliest time possible. If no")
    print("end time is selected the system will go to the latest record possible. If no start or ")
    print("end time are selected, the system will select all records.\n")
    # Exit the application (normally)
    sys.exit(0)
else:
    # --------------------
    # Clean up input for the main class
    # --------------------
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

    # ---------------
    # Actually process the request
    # ---------------

    # Create and instance of the class
    sns = SnSMessenger.SnSMessenger(topic=topic, start=start, end=end, pointer='SnsArchive2017')
    # Build a list of files
    sns.fetchFileList()
    sns.processFiles()
