import requests
# res = requests.get("http://naver.com")
res2 = requests.get("http://vkje2oigw223.com")
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


