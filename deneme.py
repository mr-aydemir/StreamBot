# selenium 3

from selenium.webdriver.common.by import By
import time
import os
# selenium 3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
PcName="EmreAydemir"
default_release_path=f"C:/Users/{PcName}/AppData/Roaming/mozilla/Firefox/Profiles"
Folders=os.listdir (default_release_path)
print(Folders)
ReleaseFolder =[x for x in Folders if "release" in  x ][0]
print(ReleaseFolder)


profile = webdriver.FirefoxProfile(
  default_release_path+"/"+ReleaseFolder  )

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=profile,
                           desired_capabilities=desired)


username = "BarışÖzcan"
url =f"https://www.youtube.com/c/{username}/videos"
driver.get(url)
##thumbnail
##video-title
##video-title
#time.sleep(3)
video_titles=driver.find_elements(By.CSS_SELECTOR, "#video-title")
video_titles[0].click()

time.sleep(1000)