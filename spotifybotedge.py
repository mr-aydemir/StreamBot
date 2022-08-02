from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# selenium 3 driver tanımlanması
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

# driver kurulumunu burda bul
# https://pypi.org/project/webdriver-manager/#use-with-edge
username= "tarimtanyeri@gmail.com"
password= "Abrakadabra12"

# Gerekli metotların oluşturulması

# selectora sahip tüm elementleri getir
def getElementList(selector):
    return driver.find_elements(By.CSS_SELECTOR, selector)

# selectora sahip ilk elementi getir
def getElement(selector):
    return driver.find_element(By.CSS_SELECTOR, selector)

# inputun doldurulup devam et denilmesi
def set_input_next(selector, username):
    ele= getElement(selector)
    ele.click()
    ele.send_keys(username)
    ele.send_keys(Keys.RETURN)

# element ekrana gelene kadar max 5 sn bekle
def waitElement(Selector):
    timeout = 5
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selector)))
    except TimeoutException:
        print("Timed out waiting for page to load")

# elemente tıkla
def clickElement(selector):
    getElement(selector).click()


# elementi bekle ve tıkla
def wait_and_click_element(selector):
    waitElement(selector)
    clickElement(selector)

# url'yi aç
def open_url(url):
    driver.get(url)

# Bot aşamaları
open_url("https://accounts.spotify.com/tr/login") # spotify login aç
set_input_next("#login-username", username) # username gir
set_input_next("#login-password", password) # password gir
wait_and_click_element("button[data-testid='web-player-link']") # web player butonunun oluşmasını bekle ve tıkla
wait_and_click_element(".GlueDropTarget--playlists.GlueDropTarget--folders") # oluşturmuş olunan ilk listenin oluşmasını bekle ve tıkla
wait_and_click_element("div[data-testid='action-bar-row'] button[data-testid='play-button']") # play butonun gelmesini bekle ve tıkla

time.sleep(1000)