import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import mailosaur
from bs4 import BeautifulSoup
from mailosaur.models import SearchCriteria
from mailosaur import MailosaurClient

driver = webdriver.Chrome()

driver.maximize_window


# Mailosaur setup
MAILOSAUR_API_KEY = 'XZMQFOoiIjWP6mvo9CD38CadKoAS8uA8'
SERVER_ID = 'nssze1dz'
# client = mailosaur.MailosaurClient(MAILOSAUR_API_KEY)

mailosaur = MailosaurClient(MAILOSAUR_API_KEY)

# Generate a random email address for testing
email_address = f'testtokped@{SERVER_ID}.mailosaur.net'

# Open the webpage and perform actions that trigger an email
driver.get("https://www.tokopedia.com/")

# For example, fill out a form to sign up
driver.find_element(By.CLASS_NAME, 'css-6c86hb').click()
# time.sleep(5)
driver.find_element(By.ID, 'input-phone-email').send_keys(email_address)
driver.find_element(By.CLASS_NAME, 'css-kt8ee4').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'css-vhz208').click()
# time.sleep(10)
# driver.find_element(By.CLASS_NAME, 'css-1qoa3eh').click()

# Wait for the email to arrive
criteria = SearchCriteria()
criteria.sent_to = email_address
email = mailosaur.messages.get(SERVER_ID, criteria, timeout=30000)

print("Subject: " + email.subject)

# # Parse the email content to extract the OTP code
# soup = BeautifulSoup(email.html.body, 'html.parser')
# otp_code = soup.find(string=lambda text: 'Your OTP code is' in text).split()[-1]

# # Print the OTP code to verify
# print(f'OTP Code: {otp_code}')

# time.sleep(5)

# # Enter the OTP code into the website
# otp_input = driver.find_element(By.TAG_NAME, 'input')
# otp_input.send_keys(otp_code)

# time.sleep(5)
# driver.find_element(By.CLASS_NAME, 'css-isbo03 e2sn3zw0')

# Wait for the user to press Enter before closing the browser
input("Press Enter to close the browser and end the script...")

# Close the browser
driver.quit()



