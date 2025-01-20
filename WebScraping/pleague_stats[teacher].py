import requests
from bs4 import BeautifulSoup
import pandas as pd


seasons = ['2022-23', '2023-24', '2024-25']
game_types = {'熱身賽': 1, '例行賽': 2, '季後賽': 3, '總冠軍賽': 4}

team_stats = dict()
for season in seasons:
    for game_type_str, game_type_no in game_types.items():
    
        pleague_url = f"https://pleagueofficial.com/stat-team/{season}/{game_type_no}#record"
        
        print('Requesting', pleague_url, end='...')
        
        # Request the url
        r = requests.get(pleague_url)
        if r.status_code != requests.codes.ok:
            print(f'Failed to access {pleague_url}')
            exit()
        
        
        # Parse the html page    
        soup = BeautifulSoup(r.text, "lxml")
        
        div_tags = soup.find_all(class_='container-fluid pb-5')
        for div_tag in div_tags:
            stat_type = div_tag.h1.text # 球隊數據╱進攻 or 球隊數據╱防守
            
            if not stat_type in team_stats.keys():
                team_stats[stat_type] = list()
            
            table_tags = div_tag.find_all('table')
            for table_tag in table_tags:        
                # 表格標題(即第一列)
                th_tags = table_tag.find('thead').find_all('th')
                
                # 表格剩下的所有列資料
                tr_tags = table_tag.find('tbody').find_all('tr')
                for tr_tag in tr_tags:
                    team_stat = dict()
                    # 第一欄(是標題欄)
                    team_stat[th_tags[0].text] = tr_tag.th.a.text
                    # 剩下的所有欄資料
                    td_tags = tr_tag('td')
                    for i in range(len(td_tags)):
                        team_stat[th_tags[i+1].text] = td_tags[i].text
                    team_stat['賽季'] = season
                    team_stat['類型'] = game_type_str
                        
                    team_stats[stat_type].append(team_stat)

        print('done')
        
for stat_type, stat_data in team_stats.items():
    df = pd.DataFrame(stat_data)
    df.to_csv(f'{stat_type}.csv')
