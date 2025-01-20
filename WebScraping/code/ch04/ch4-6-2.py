from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element(by=By.XPATH, value='//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(by=By.XPATH, value='//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()
