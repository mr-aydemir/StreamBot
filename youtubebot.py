from selenium.webdriver.common.by import By
import time
from WebBot import WebBot
if __name__ == "__main__":
    bot = WebBot()
    # Bot aşamaları
    #region Kullanıcıya ait ilk videoyu aç
    username = "BarışÖzcan"
    bot.open_url(f"https://www.youtube.com/c/{username}/videos")
    bot.wait_and_click_element("#video-title") # ilk videoyu aç
    #endregion Kullanıcıya ait ilk videoyu aç
    time.sleep(1000) # 1000 saniye bekle tarayıcının kapanmaması için
