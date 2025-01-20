from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup
import lxml

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://tpbl.basketball/stats/players')
driver.implicitly_wait(5)

seasons=['2024-25 賽季']
game_types=['例行賽','熱身賽']
# 定位賽季:
# //*[@id="__nuxt"]/main/div/article/section[3]/div[2]/div/div[2]/div[1]/select

season_dropdown_element = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/main/div/article/section[3]/div[2]/div/div[2]/div[1]/select')
select_season = Select(season_dropdown_element)
select_season.select_by_visible_text(seasons[0])



stat_all=dict()
for g in game_types:
    print()
    # 定位比賽種類選單盒:
    # //*[@id="__nuxt"]/main/div/article/section[3]/div[2]/div/div[2]/div[2]/select
    gametype_dropdown_element = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/main/div/article/section[3]/div[2]/div/div[2]/div[2]/select')
    select_gametype = Select(gametype_dropdown_element)
    select_gametype.select_by_visible_text(g)
    
    # 定位查詢出來的球員資料 table:
    # //*[@id="vgt-table"]
    get_table=driver.find_element(By.XPATH, '//*[@id="vgt-table"]')
    # print(get_table.tag_name)
    # print(get_table.get_attribute('innerHTML'))
    soup=BeautifulSoup(get_table.get_attribute('innerHTML'),"lxml")
    
    
    players=[]
    h1=[]
    
    
    #vgt-table > thead > tr > th:nth-child(1) > span:nth-child(2)
    tag_thead=soup.select("thead tr th")
    i=0
    for e in tag_thead:
        print(e.select("span")[1].text, end=', ')
        i+=1
        h1.append(e.select("span")[1].text)
    print()
    
    tag_tr=soup.select("tbody tr")
    print(len(tag_tr),type(tag_tr))
    
    
    n=0
    for tr in tag_tr:
        rec=[]
        tmp_dict=dict()
        for td in tr.select("td"):
            print(td.select("span")[0].text,end=',')
            rec.append(td.select("span")[0].text)
        print()
        for k,v in zip(h1,rec):
            tmp_dict[k]=v
        
        players.append(tmp_dict)
        # print("="*16)
    
    
    stat_all[g]=players
    
    
    time.sleep(5)



#2345678
driver.quit()

print(players)
print("="*32)
print(stat_all)
