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
driver.get("https://www.tokopedia.com/")


