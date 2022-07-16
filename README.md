# Misc-Python-Scripts
Two Python scripts that came from a recent school project.

# ReservationMaker.py
A script that takes advantage of the Selenium webdriver to automatically take in a string w/ info provided by the user and automatically fill out the room reservation form for OkState's library rooms. Takes users up to the page where they have to enter school credentials, which is purposely not filled in by the program in interest of security. Requires the included chromedriver files in the same folder (according to your operating system) to be able to function. 
Credit for chromedriver:
https://chromedriver.chromium.org/downloads

I may implement this file into a basic website in the future for reference.

# EventEmailHandler.py
Program that sends a reminder emails to those signed up for a specific event. Takes in a string that parses the following data from the string: event name, event date, event time, and list of emails to send the reminder to. If used, it will require an email and password to be provided in order to actually send.

