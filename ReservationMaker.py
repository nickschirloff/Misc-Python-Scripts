from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import time, date, datetime, timedelta
from selenium.webdriver.support.ui import Select
import os
import sys

# TODO: Get new input from user if reservation room at a datetime is not available
# TODO: Maybe create method for room blacklist?
# TODO: Try block to check for incorrect dates

class Reservation:
    # Directing the driver path to install location
    try:
        f = os.path.join(os.getcwd(),"chromedriver(Windows).exe")
        driver = webdriver.Chrome(f)
    except:
        print("Error loading driver")
    # There isn't a decent way to hide the window until its needed,
    # so we minimize it until the point where the user enters
    # their account credentials on the OSU webpage
    #driver.minimize_window()
    # Getting the webpage
    driver.get('https://spaces.library.okstate.edu/')

    ## Init
    def __init__(self, user_date, user_seats, user_time, user_floor):
        self.user_date = user_date
        self.user_seats = user_seats
        self.user_time = user_time
        self.user_floor = user_floor
        try:
            create_reservation(self.user_date, self.user_seats, self.user_time, self.user_floor)
        except:
            print("invalid parameters")
    # Returns string value that represents any errors that occurred
    def create_reservation(self):
        date = ""
        if self.user_date == "Today":
            date = datetime.today().strftime('%Y-%m-%d')
        elif self.user_date == "Tomorrow":
            date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        elif datetime.strptime(self.user_date,'%Y-%m-%d').date() < datetime.today().date():
            self.driver.close()
            return "Error: Selected time has passed."
        else:
            date = self.user_date

        try:
            # Getting and setting the calendar value
            date_element = self.driver.find_element_by_id("date")
            date_element.click()
            self.driver.find_element_by_id("date").clear()
            date_element.send_keys(date)
        except:
            self.driver.close()
            print("Invalid or unavailable date selected.")

        # Getting the seats drop down menu and selecting the input number of required seats
        time_string = "#seatsDropDown [value=\'" + str(self.user_seats) + "\'"
        self.driver.find_element_by_css_selector(time_string).click()
        # Getting the required floor number from the drop down and selecting it
        floor_string = "#floorDropDown [value=\'" + str(self.user_floor) + "\'"
        self.driver.find_element_by_css_selector(floor_string).click()

        # Getting the grid path of the available times, selecting the first one that fits whats required
        grid_xml_path = '/html/body/div[1]/section/div[2]/div/div/div[1]/div/div[2]/div[2]'
        time_button_text = "//button[contains(text(), \'" + self.user_time + "\')]"
        buttons = self.driver.find_elements_by_xpath(time_button_text)
        # If there are no buttons with the user's time, return
        if not buttons:
            self.driver.close()
            return "No rooms are available. Change your parameters."
        else:
            buttons[0].click()

        # Set path of the confirm button, and then click it
        # TODO: Allow for time in other rooms to be chosen?
        confirm_path = self.driver.find_element_by_xpath('//button[normalize-space()="Confirm"]').click()
        #self.driver.maximize_window()
        print("Ran successfully")
        return "Ran successfully"

r1 = Reservation("4-21-2022","1","2","2")
r1.create_reservation()
