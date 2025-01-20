from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://tpbl.basketball/stats/players')
driver.implicitly_wait(5)

game_types = ['例行賽', '熱身賽']
data_types = ['場均數據', '累積數據']

player_stats = []

for game_type in game_types:
    game_type_element = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/main/div/article/section[3]/div[2]/div/div[2]/div[2]/select')
    
    select_game_type = Select(game_type_element)
    select_game_type.select_by_visible_text(game_type)
    
    for data_type in data_types:
        data_type_element = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/main/div/article/section[3]/div[2]/div/div[2]/div[6]/select')
        
        select_data_type = Select(data_type_element)
        select_data_type.select_by_visible_text(data_type)
        
        
        # find talbe element
        tag_table = driver.find_element(By.XPATH, '//*[@id="vgt-table"]')
        
        # construct soup object from the table element
        soup = BeautifulSoup(tag_table.get_attribute('innerHTML'), "lxml")
        
        # retrieve column names
        column_names = ['競賽類型', '資料類型']
        tags_th = soup.find_all('th')
        for tag_th in tags_th:
            tags_span = tag_th.find_all('span')
            column_names.append(tags_span[1].text)
            # print(tags_span[1].text)
    
            
        # retrieve each player's record
        tag_tbody = soup.find('tbody')
        tags_tr = tag_tbody.find_all('tr')
        for tag_tr in tags_tr:
            column_data = [game_type, data_type]
            tags_td = tag_tr.find_all('td')
            for i, tag_td in enumerate(tags_td):
                if i == 1: # 球員姓名
                    tag_h6 = tag_td.span.div.div.find_next_sibling().h6
                    column_data.append(tag_h6.text)
                    # print(tag_h6.text)
                elif i == 2: # 球隊的影像
                    tag_div = tag_td.span.div
                    tag_img = tag_div.find('img')
                    column_data.append(tag_img['src'])
                    # print(tag_img['src'])
                else:
                    column_data.append(tag_td.span.text)
                    # print(tag_td.span.text)
            result = dict(zip(column_names, column_data))
            player_stats.append(result)
            # print(result)
    
    
        time.sleep(5)
        
print(len(player_stats))
print(player_stats[0])

df = pd.DataFrame(player_stats)
df.to_csv('tpbl_player_stats.csv')

driver.quit()