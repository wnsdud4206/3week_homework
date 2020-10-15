import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# bs4 는 함수??
# requests도 외부 라이브러리고 BeautifulSoup도 외부 라이브러리면 하는일은 무엇?

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

music = soup.select('div.music-list-wrap > table.list-wrap > tbody > tr.list')
# print(music)

for mus in music:
    # .text[0:2] index 0부터 1까지 출력, .text[1:3] index 1부터 2까지 출력
    # ex) .text[i:j] -> i ~ (j-1)
    number = mus.select_one("td.number").text[0:2].rstrip()
    title = mus.select_one("td.check > input")["title"]
    artist = mus.select_one("td.info > a.artist").text
    # print(number, title, artist)
    doc = {
        "number": number,
        "title": title,
        "artist": artist
    }
    print(doc)
    # db.genie_chart.insert_one(doc)

# genie_chart = db.genie_chart.find({})
# for chart in genie_chart:
#     print(chart["number"], chart["title"], chart["artist"])

