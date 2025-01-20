#
import requests
from bs4 import BeautifulSoup
import lxml
import random

header1={
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
}
header2={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
header3={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}
header4={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"
}

headers_list=[header1,header2,header3,header4]

stat_team_url="https://pleagueofficial.com/stat-team/"

headers=random.choice(headers_list)

result=requests.get(stat_team_url, headers=headers)
soup=BeautifulSoup(result.text,"lxml")
f=open("output.csv","w")
#==== get how many options
for container in soup.find_all("div",attrs={"class":"container-fluid pb-5"}):
    # print(len(container.select("h1")) )
    
    print(container.select("h1")[0].text)  # 印 table名稱
    f.write(container.select("h1")[0].text+'\n')
    for tbl in container.select("table"):
        for e in tbl.select("thead tr th"): # 印 table head
            print(e.text, end=',')
            f.write(e.text+',')
        print()
        f.write('\n')
        # print(tbl.select("tbody tr th")[0].text, end=',')
        
        # 印 table body        
        for e in tbl.select("tbody tr"):
            
            print(e.select("th")[0].text, end=',')  # 拆開問題,     tr[0].th[0].text才是本紀錄第一個欄位值
            f.write(e.select("th")[0].text+',')
            for rec in e.select('td'):              # 接下來就迴圈, tr[1:].td[0].text
                print(rec.text, end=',')
                f.write(rec.text+',')
            print()
            f.write('\n')
            # print(e.text, end=',')
        print()
        
# print(soup.text)
f.close()