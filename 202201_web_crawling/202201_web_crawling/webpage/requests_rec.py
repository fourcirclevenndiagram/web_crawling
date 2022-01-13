import requests
res = requests.get("http://naver.com")
print("応答コード : ", res.status_code) # 200なら正常
