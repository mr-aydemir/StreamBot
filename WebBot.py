from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class WebBot():
    def __init__(self) -> None:
        import undetected_chromedriver.v2 as uc
        self.driver = uc.Chrome(version_main=103)
        """
        from selenium import webdriver
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # selenium 3 driver tanımlanması
        # driver kurulumunu burda bul
        # https://pypi.org/project/webdriver-manager/#use-with-edge
        """

    # Gerekli metotların oluşturulması
    # selectora sahip tüm elementleri getir
    def getElementList(self, selector: str):
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    # selectora sahip ilk elementi getir
    def getElement(self, selector: str):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    # inputun doldurulup devam et denilmesi
    def set_input_and_next(self, selector: str, username: str):
        ele = self.getElement(selector)
        ele.click()
        ele.send_keys(username)
        ele.send_keys(Keys.RETURN)

    # element ekrana gelene kadar max 5 sn bekle
    def waitElement(self, selector: str):
        timeout = 5
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            return True
        except TimeoutException:
            print("Timed out waiting for page to load")
            return False

    # elemente tıkla
    def clickElement(self, selector: str):
        self.getElement(selector).click()

    # elementi bekle ve tıkla
    def wait_and_click_element(self, selector: str):
        if not self.waitElement(selector):
            return False
        self.clickElement(selector)
        return True

    # url'yi aç
    def open_url(self, url: str):
        self.driver.get(url)

    def wait(self, seconds):
        WebDriverWait(self.driver, seconds)
