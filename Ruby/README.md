
Technologies used
-----------------------------------------------------------------------------------------
Ruby 2.5, Sinatra

Settings and notes
-----------------------------------------------------------------------------------------
Set the path to Windows if not configured.

SETX PATH "%PATH%;C:\Ruby25-x64\bin"

Needed to install.

gem install sinatra

Script to be executed.

ruby app.rb

Endpoints
-----------------------------------------------------------------------------------------
1. localhost:8080/hello
2. localhost:8080/param?key1=AAA&key2=BBB
3. localhost:8080/text/AAABBB
