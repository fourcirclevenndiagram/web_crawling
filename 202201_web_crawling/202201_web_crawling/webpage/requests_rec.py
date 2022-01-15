import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
# res = requests.get("http://naver.com")
res2 = requests.get(url, headers=headers)
# print("応答コード : ", res.status_code) # 200なら正常
print("応答コード : ", res2.status_code) # 200なら正常
res2.raise_for_status()
print("ウェブスクレイピングを開始します")
# if res.status_code == requests.codes.ok:
#     print("正常です")
# else:
#     print("問題が発生しました。[エラーコード ", res.status_code, "]")
# 
# if res2.status_code == requests.codes.ok:
#     print("正常です")
# else:
#     print("問題が発生しました。[エラーコード ", res2.status_code, "]")

# res.raise_for_status()                   # Exception has occurred: HTTPError
# print("ウェブスクレイピングを開始します")   # Exception has occurred: HTTPError

print(res2.text)
with open("mynadocoding.html", "w", encoding="utf8") as f:
    f.write(res2.text)
    


