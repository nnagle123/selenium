from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
# for video 1, 2, 3
# driver.get("https://techwithtim.net")
# for video 4
driver.get("https://orteil.dashnet.org/cookieclicker/")

# ====================================================================
# Video 2
# Go into the search bar, type a search, hit enter, pull elements from site, close driver.

# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     print(main.text)

#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry-summary")
#         print(header.text)

# finally:
#     driver.quit()

# ============================================================================

# Video 3
# Go to website, click on a link, then on the new page click on a button, then just for fun go back, back, back, forward, forward

# link = driver.find_element_by_link_text("Python Programming")
# link.click()

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()

#     element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     element.click()

#     driver.back()
#     driver.back()
#     driver.back()
#     driver.forward()

# except:
#     driver.quit()

# ===============================================================================
# Video 4 
#  In this video we created a bot that clicks on cookies on a cookie clicking website then buys products that make more cookies.  


driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
# items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(50000000000):
    actions.perform()
    # count = int(cookie_count.split(" ")[0])
    # for item in items:
    #     value = int(item.text)
    #     if value <= count:
    #         upgrade_actions = ActionChains(driver)
    #         upgrade_actions.move_to_element(item)
    #         upgrade_actions.double_click()
    #         upgrade_actions.perform()


