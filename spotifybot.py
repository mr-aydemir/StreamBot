# selenium 3

from click import password_option
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
# selenium 3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager

def waitElement(Selector):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, Selector))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")  



driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
username= "tarimtanyeri@gmail.com"
password= "Abrakadabra12"

url ="https://accounts.spotify.com/tr/login"
driver.get(url)
ele= driver.find_element(By.CSS_SELECTOR, "#login-username")
ele.click()
ele.send_keys(username)
ele.send_keys(Keys.RETURN)
#driver.execute_script(f"arguments[0].setAttribute('value','{username}')", ele)

ele= driver.find_element(By.CSS_SELECTOR, "#login-password")
#driver.execute_script(f"arguments[0].setAttribute('value','{password}')", ele)
ele.click()
ele.send_keys(password)
ele.send_keys(Keys.RETURN)



time.sleep(5)
video_titles=driver.find_elements(By.CSS_SELECTOR, "button[data-testid='web-player-link']")
video_titles[0].click()

waitElement(".GlueDropTarget--playlists.GlueDropTarget--folders")
video_titles=driver.find_elements(By.CSS_SELECTOR, ".GlueDropTarget--playlists.GlueDropTarget--folders")
video_titles[0].click()



waitElement("button[data-testid='play-button']")
video_titles=driver.find_elements(By.CSS_SELECTOR, "button[data-testid='play-button']")
video_titles[1].click()

time.sleep(1000) 