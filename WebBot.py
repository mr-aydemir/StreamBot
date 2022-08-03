from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class WebBot():
    def __init__(self, driver) -> None:
        self.driver:WebDriver = driver

    # Gerekli metotların oluşturulması
    # selectora sahip tüm elementleri getir
    def getElementList(self, selector:str):
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    # selectora sahip ilk elementi getir
    def getElement(self, selector:str):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    # inputun doldurulup devam et denilmesi
    def set_input_and_next(self, selector:str, username:str):
        ele= self.getElement(selector)
        ele.click()
        ele.send_keys(username)
        ele.send_keys(Keys.RETURN)

    # element ekrana gelene kadar max 5 sn bekle
    def waitElement(self, selector:str):
        timeout = 5
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        except TimeoutException:
            print("Timed out waiting for page to load")

    # elemente tıkla
    def clickElement(self, selector:str):
        self.getElement(selector).click()


    # elementi bekle ve tıkla
    def wait_and_click_element(self, selector:str):
        self.waitElement(selector)
        self.clickElement(selector)

    # url'yi aç
    def open_url(self, url:str):
        self.driver.get(url)
