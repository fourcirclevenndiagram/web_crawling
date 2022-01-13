import requests
# res = requests.get("http://naver.com")
res = requests.get("https://pinocc.tistory.com/198")
res2 = requests.get("http://google.com")
print("応答コード : ", res.status_code) # 200なら正常
print("応答コード : ", res2.status_code) # 200なら正常
