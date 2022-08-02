from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# selenium 3
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver kurulumunu burda bul
# https://pypi.org/project/webdriver-manager/#use-with-edge
username= "tarimtanyeri@gmail.com"
password= "Abrakadabra12"

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
def set_input(selector, username):
    ele= driver.find_element(By.CSS_SELECTOR, selector)
    ele.click()
    ele.send_keys(username)
    ele.send_keys(Keys.RETURN)

def waitElement(Selector):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, Selector))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
def clickElement(selector):
    driver.find_element(By.CSS_SELECTOR, selector).click()


url ="https://accounts.spotify.com/tr/login"
driver.get(url)

set_input("#login-username", username)
set_input("#login-password", password)

waitElement("button[data-testid='web-player-link']")
clickElement("button[data-testid='web-player-link']")

waitElement(".GlueDropTarget--playlists.GlueDropTarget--folders")
clickElement(".GlueDropTarget--playlists.GlueDropTarget--folders")

waitElement("button[data-testid='play-button']")
clickElement(".GlueDropTarget--playlists.GlueDropTarget--folders")

driver.find_elements(By.CSS_SELECTOR, "button[data-testid='play-button']")[1].click()

time.sleep(1000)