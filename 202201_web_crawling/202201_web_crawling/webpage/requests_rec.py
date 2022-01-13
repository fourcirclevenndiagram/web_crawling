import requests
# res = requests.get("http://naver.com")
res = requests.get("http://dnet.nkcnet.co.jp/scripts/dneo/dneo.exe?")
res2 = requests.get("http://google.com")
print("応答コード : ", res.status_code) # 200なら正常
print("応答コード : ", res2.status_code) # 200なら正常

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
res2.raise_for_status()
print("ウェブスクレイピングを開始します")