# Selenium

# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Step 1 - Enter google and search for ynetnews
browser = webdriver.Chrome('D:\Technology\Programming\Python\Selenium\chromedriver')
browser.get('https://www.google.com')
search = browser.find_element_by_name('q')  # Click on the search button.
search.send_keys("Ynetnews")  # Enter the word in the search.
search.send_keys(Keys.RETURN)  # Send the words to google.
time.sleep(5)  # Wait for the results


# Step 2 - Find the ynet link, enter it and verify that it is correct
ynet = browser.find_element_by_class_name('ellip')  # Finds element using class name.
ynet.click()  # Clicks on the link.
time.sleep(5)  # Wait for the page to load.
url = browser.current_url
if "www.ynetnews.com" not in url:
    raise Exception("Incorrect URL!")


# Find and print current temperature
temperature = browser.find_element_by_id('cdanwmansrch_weathertemps').text  # Temperature string value
print("The current temperature is: {}".format(temperature))


# Change the city to Eilat and print the weather
city = browser.find_element_by_id('cdanwmansrch_weathercitieselect')  # Represents the city dropdown list
city.send_keys('Eilat')  # Change the city to Eilat.
time.sleep(5)  # Wait for the webpage to react.
temperature = browser.find_element_by_id('cdanwmansrch_weathertemps').text  # Temperature string value
print("The temperature of Eilat is: ", temperature)





