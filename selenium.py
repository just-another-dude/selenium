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
time.sleep(3)
browser.get('https://www.google.com')
time.sleep(3)
search = browser.find_element_by_name('q')  # Click on the search button.
search.send_keys("Ynetnews")  # Enter the word in the search.
search.send_keys(Keys.RETURN)  # Send the words to google.
time.sleep(3)  # Wait for the results


# Find the ynet link, enter it and verify that it is correct
ynet = browser.find_element_by_class_name('ellip')  # Finds element using class name.
ynet.click()  # Clicks on the link.
time.sleep(3)  # Wait for the page to load.
url = browser.current_url
if "www.ynetnews.com" not in url:
    raise Exception("Incorrect URL!")


# Find and print current temperature
temperature = browser.find_element_by_id('cdanwmansrch_weathertemps').text  # Temperature string value
print("The current temperature is: {}".format(temperature))


# Change the city to Eilat and print the weather
city = browser.find_element_by_id('cdanwmansrch_weathercitieselect')  # Represents the city dropdown list
city.send_keys('Eilat')  # Change the city to Eilat.
time.sleep(2)  # Wait for the webpage to react.
temperature = browser.find_element_by_id('cdanwmansrch_weathertemps').text  # Temperature string value
print("The temperature of Eilat is: ", temperature)


# Set page resolution to 1920*1080
browser.set_window_size(1920, 1080)
time.sleep(3)
# size = browser.get_window_size()
# print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))


# Enter the main article on the page
article = browser.find_element_by_class_name('subtitle')  # Object representing the main article
article.click()  # Clicking on the article.
time.sleep(3)


# Verify that a "send to friend" link exists, if not - raise an appropriate exception.
try:
    # send_friend = browser.find_element_by_class_name('sprite_article_asb_send_tofriend_icon')
    send_friend = browser.find_element_by_link_text('send to friend')
	print('The "send to friend" link exists!')
except selenium.common.exceptions.NoSuchElementException:
    raise Exception('The "send to friend" link does not exist!')
except Exception as error:
    raise Exception("The following unexpected error has occured: {0}".format(error))


# Enter the "send_to_friend" link
href = send_friend.get_attribute('href')  # Link to the "send to friend" page.
half_link = re.search(pattern = "\(.+\)", string = href).group()  # Regex to isolate path to html file.
modified_link = half_link.replace("('", "").replace(")", "")  # Removing useless characters.
full_link = "https://www.ynetnews.com" + modified_link  # Full link to the "send to friend" HTML page.
browser.get(full_link)  # Load the "send to friend" webpage.
time.sleep(2)


# Enter the relevant information in the boxes
recipient = browser.find_element_by_name('txtTo')  # Object representing the recipient box.
recipient.send_keys('recipient@mail.com')  # Type in the recipient email.
sender_name = browser.find_element_by_name('txtFromName')  # Sender's name box.
sender_name.send_keys("Sender's Name")  # Type in the sender's name.
sender_email = browser.find_element_by_name('txtFromAddress')  # Sender's email box.
sender_email.send_keys('sender@mail.com')  # Type in sender's mail.
comments = browser.find_element_by_name('txtRemarks')  # Comment box.
comments.send_keys('Some comments')  # Type in some comments.


# Switch to captcha iframe.
# Important Note: If there are multiple iframes, a list containg the iframe objects will be created.
iframe = browser.find_element_by_tag_name("iframe")  # Object representing the captcha.
browser.switch_to.frame(iframe)  # Switching to the captcha object since it's an iframe.


# Access class using the CSS selector since selenium doesn't support compound class names (classe names with spaces)
error_message = browser.find_element_by_css_selector('.rc-anchor-center-item.rc-anchor-error-message')
if error_message:
    print("There is a captcha error message:\n", error_message)


# Switch back to main page
browser.switch_to.default_content()
