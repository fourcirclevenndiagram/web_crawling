import re
# abcd, book, desk
# ca?e -> care, cafe, case, cave
# caae, cabe, cace, ...

p = re.compile("ca.e")
# . (ca.e) : 一つの文字     ex) care, cafe, case // caffe (X)
# ^ (^de)  : 文字列の始まり ex) desk, destination  // fade (X)
# $ (se$)  : 文字列の最後   ex) case, base // face (X)

m = p.match("caffe")
n = p.match("case")
# print(m.group())    # マッチングに失敗したのでエラー発生
print(n.group())      # マッチングに成功したので正常終了