# Selenium

# Standard Library Modules
import re  # Used for regex
import time  # Used for sleep.

# Third-Party Modules
from selenium import webdriver  # Used for opening a browser session.
from selenium.webdriver.common.keys import Keys  # Used for sending values in a search bar.
from selenium.webdriver.chrome.options import Options  # Used for resolution.
import selenium  # Used for error handling


# Enter google and search for ynetnews
browser = webdriver.Chrome('D:\Technology\Programming\Python\Selenium\chromedriver')
browser.get('https://www.google.com')
search = browser.find_element_by_name('q')  # Click on the search button.
search.send_keys("Ynetnews")  # Enter the word in the search.
search.send_keys(Keys.RETURN)  # Send the words to google.
time.sleep(5)  # Wait for the results


# Find the ynet link, enter it and verify that it is correct
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


# Set page resolution to 1920*1080
browser.set_window_size(1920, 1080)
time.sleep(5)
# size = browser.get_window_size()
# print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))


# Enter the main article on the page
article = browser.find_element_by_class_name('subtitle')  # Object representing the main article
article.click()  # Clicking on the article.
time.sleep(5)


# Verify that a "send to friend" link exists, if not - raise an appropriate exception.
try:
    send_friend = browser.find_element_by_link_text('send to friend')
    # send_friend = browser.find_element_by_class_name('sprite_article_asb_send_tofriend_icon')
	print('The "send to friend" link exists!')
except selenium.common.exceptions.NoSuchElementException:
    raise Exception('The "send to friend" link does not exist!')
except Exception as error:
    raise Exception("The following unexpected error has occured: {0}".format(error))


# Enter the "send_to_friend" link
# send_friend.click()
# time.sleep(5)
href = send_friend.get_attribute('href')  # Link to the "send to friend" page.
half_link = re.search(pattern = "\(.+\)", string = href).group()  # Regex to isolate path to html file.
modified_link = half_link.replace("('", "").replace(")", "")  # Removing useless characters.
full_link = "https://www.ynetnews.com" + modified_link  # Full link to the "send to friend" HTML page.
