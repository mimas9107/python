from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://mops.twse.com.tw/mops/web/t163sb01')
driver.implicitly_wait(5)

isnew = ['歷史資料']
seasons = ['1', '2', '3', '4']
years = ['108', '109', '110', '111', '112']
compand_id = '2330'

isNew_dropdown_element = driver.find_element(By.XPATH, '//*[@id="isnew"]')
select_isNew = Select(isNew_dropdown_element)
select_isNew.select_by_visible_text(isnew[0])

companyID_text_element = driver.find_element(By.XPATH, '//*[@id="co_id"]')
companyID_text_element.send_keys(compand_id)
companyID_text_element.send_keys(Keys.ENTER)

for year in years:
    for season in seasons:
        year_element = driver.find_element(By.XPATH, '//*[@id="year"]')
        season_dropdown_element = driver.find_element(By.XPATH, '//*[@id="season"]')
        submit_button_element = driver.find_element(By.XPATH, '/html/body/center/table/tbody/tr/td/div[4]/table/tbody/tr/td/div/table/tbody/tr/td[3]/div/div[3]/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div/input')

        year_element.clear()
        year_element.send_keys(year)

        select_season = Select(season_dropdown_element)
        select_season.select_by_visible_text(season)

        # time.sleep(5)
        #
        submit_button_element.click()

        time.sleep(5)

driver.quit()