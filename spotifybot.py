
from WebBot import WebBot
import time

if __name__ == "__main__":
    # selenium 3 driver tanımlanması
    # driver kurulumunu burda bul
    # https://pypi.org/project/webdriver-manager/#use-with-edge
    from selenium import webdriver
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    bot = WebBot(driver)

    username= "tarimtanyeri@gmail.com"
    password= "Abrakadabra12"
    # Bot aşamaları
    
    # Giriş Yap
    bot.open_url("https://accounts.spotify.com/tr/login") # spotify login aç
    bot.set_input_and_next("#login-username", username) # username gir ve bir sonrakine ilerle
    bot.set_input_and_next("#login-password", password) # password gir ve bir sonrakine ilerle
    bot.wait_and_click_element("button[data-testid='web-player-link']") # web player butonunun oluşmasını bekle ve tıkla

    # Müzik Listesini aç
    bot.wait_and_click_element(".GlueDropTarget--playlists.GlueDropTarget--folders") # oluşturmuş olunan ilk listenin oluşmasını bekle ve tıkla
    bot.wait_and_click_element("div[data-testid='action-bar-row'] button[data-testid='play-button']") # play butonun gelmesini bekle ve tıkla
    time.sleep(1000) # 1000 saniye bekle tarayıcının kapanmaması için