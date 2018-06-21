
Technologies used
-----------------------------------------------------------------------------------------
Python 3, Flask

Settings and notes
-----------------------------------------------------------------------------------------
Set the path to Windows if not configured.

SETX PATH "%PATH%;C:\Python\Python36\Scripts"

Needed to install.

1. py -m pip install --user virtualenv
2. pip install flask flask-jsonpify flask-sqlalchemy flask-restful

Script to be executed.

py app.py

Endpoints
-----------------------------------------------------------------------------------------
1. localhost:8080/
2. localhost:8080/param?key1=AAA&key2=BBB
3. localhost:8080/text/AAABBB
