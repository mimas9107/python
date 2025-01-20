from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

# tags = soup("li")
# tag = tags[1]
for tag in soup("body"):
    print("標籤名稱: ", tag.name)
    print("標籤內容: ", tag.text)
    print("標籤內容: ", tag.string)
# print("標籤內容: ", tag.b.string)
# print("URL網址: ", tag.get("href", None))
# print("target屬性: ", tag["target"])
    print(soup.find_all(attrs={"class","score"}))


