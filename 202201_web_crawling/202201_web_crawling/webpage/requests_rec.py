import requests
# res = requests.get("http://naver.com")
res = requests.get("https://pinocc.tistory.com/198")
res2 = requests.get("D:\05_Programming\Python\202201_web_crawling\202201_web_crawling\202201_web_crawling\webpage\main.html")
print("応答コード : ", res.status_code) # 200なら正常
print("応答コード : ", res2.status_code) # 200なら正常
