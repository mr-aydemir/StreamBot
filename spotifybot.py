from WebBot import WebBot
import time
import threading

from data.user import User
from secure.users import users

def listen_thread(user: User):
    from selenium import webdriver
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    bot = WebBot(driver)

    # region Giriş Yap
    # spotify login aç
    bot.open_url("https://accounts.spotify.com/tr/login")
    # username gir ve bir sonrakine ilerle
    bot.set_input_and_next("#login-username", user.name)
    # password gir ve bir sonrakine ilerle
    bot.set_input_and_next("#login-password", user.password)
    # web player butonunun oluşmasını bekle ve tıkla
    if not bot.wait_and_click_element("button[data-testid='web-player-link']"):
        return
    # endregion Giriş Yap

    # region Müzik Listesini aç
    # oluşturmuş olunan ilk listenin oluşmasını bekle ve tıkla
    bot.wait_and_click_element(
        ".GlueDropTarget--playlists.GlueDropTarget--folders")
    # play butonun gelmesini bekle ve tıkla
    bot.wait_and_click_element(
        "div[data-testid='action-bar-row'] button[data-testid='play-button']")
    # time.sleep(1000)  # 1000 saniye bekle tarayıcının kapanmaması için
    # endregion Müzik Listesini aç
    time.sleep(1000)


if __name__ == "__main__":
    # selenium 3 driver tanımlanması
    # driver kurulumunu burda bul
    # https://pypi.org/project/webdriver-manager/#use-with-edge
    users = users
    threads = list()
    for user in users:
        x = threading.Thread(target=listen_thread, args=(user,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()
        time.sleep(3)
