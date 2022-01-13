import requests
# res = requests.get("http://naver.com")
res = requests.get("https://pinocc.tistory.com/198")
print("応答コード : ", res.status_code) # 200なら正常
