# voltapythondemo
This repos is a programming challenge for Volta Charging.

## How To Use This Repo
There are two main components to this library. The first is a command line application. The second is a webpage application. You can run either application. However both should be run using Python 2.7+. I make no promises that this is application will work with Python 3.6+.

## What's Important About This Repo
This repo is designed to show a few things.

1. I can write reusable code (There's code here in a class that can be run in the terminal and web application)
2. Show I can write command line application that use libraries (classes) that I've written
3. Show I can write a really simply python web application that uses classes that I've written for the back end
4. Show I can tie it all together
5. Help you understand how I write code (what I see as commits and features for a small project)
6. Give you and idea of "full stack" skills

## Up and Running
In order to get started you'll first need to clone down the repo

```
git clone https://github.com/knapptimezzz/voltapythondemo.git
```

One you have that navigate to the repo and install python dependencies (assuming you have pip installed)

```
cd voltapythondemo
pip install -r requirements.txt
```

From this point you have two options. One the command line tool and the other a web application

### Command Line
To launch the command line version, type

```
python cmdline.py --help
```

To view the help menu. You have several options to choose from on the command line.

|Option|Result|
|---|---|
| no arguments | All results from the archive |
| --help | Help menu (overrides all other arguments) |
| -t | Topic you wish to search on |
| -s mm/dd/yyyy-hh:mm:ss| Start time you wish to begin from. You must have a date. Time is optional |
| -e mm/dd/yyyy-hh:mm:ss| End time you wish to search to. You must have a date. Time is optional |

Output will be in a file labeled

```
voltapythondemo/output.csv
```

### Web Application
To launch the web application, type

```
python flask_app.py
```

This will spool up a mini web server on your laptop using flask. From there you'll need to open a browser to

```
http://localhost:9090
```

And there you should see this page

![Webpage Image](static/css/images/Webpage.png)

From there you can fill out the form and submit it. When the page refreshes you can download the file with the download button.
