# voltapythondemo
This repos is a programming challenge for Volta Charging.

## How To Use This Repo
There are two main components to this library. The first is a command line application. The second is a webpage application. You can run either application. However both should be run using Python 2.7+. I make no promises that this is application will work with Python 3.6+.

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
| -s | Start time you wish to begin from |
| -e | End time you wish to search to |

### Web Application
To launch the web application, type

```
python flask_app.py
```

This will spool up a mini web server on your laptop using flask. From there you'll need to open a browser to
