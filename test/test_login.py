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

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.tokopedia.com/")

def test_login():
    driver.find_element(By.CLASS_NAME, 'css-16r70d4').click()
    time.sleep(3)
    driver.find_element(By.ID, 'email-phone').send_keys("scrumbleoreo@gmail.com")
    driver.find_element(By.ID, 'email-phone-submit').click()
    time.sleep(3)
    driver.find_element(By.ID, 'password-input').send_keys("Scrumble121*")
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/article/div/div[2]/form/button').is_displayed
    driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/article/div/div[2]/form/button').click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, 'css-isbo03 e2sn3zw0').is_displayed
    time.sleep(3)

def test_teardown():
    # Wait for the user to press Enter before closing the browser
    input("Press Enter to close the browser and end the script...")
    # Close the browser
    driver.quit()
    print("Test completed")