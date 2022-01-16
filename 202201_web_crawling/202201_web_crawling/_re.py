import re
# abcd, book, desk
# ca?e -> care, cafe, case, cave
# caae, cabe, cace, ...

p = re.compile("ca.e")
# . (ca.e) : 一つの文字     ex) care, cafe, case // caffe (X)
# ^ (^de)  : 文字列の始まり ex) desk, destination  // fade (X)
# $ (se$)  : 文字列の最後   ex) case, base // face (X)

def print_match(n):
    # m = p.match("caffe")
    
    # print(m.group())    # Exception has occurred: AttributeError. NoneType' object has no attribute 'group'
    # print(n.group())    # マッチングに成功したので正常終了
    if n:
        print("n.group(): ", n.group()) # 一致する文字列リターン
        print("n.string : ", n.string)  # 入力された文字列
        print("n.start(): ", n.start()) # 一致する文字列の最初のインデックス
        print("n.end()  : ", n.end())   # 一致する文字列の最後のインデックス
        print("n.span() : ", n.span())  # 一致する文字列の最初、最後のインデックス
    else:
        print("マッチング失敗")

n = p.match("careless") # match : 与えられた文字列の最初から一致しているか確認
print_match(n)
o = p.search("good cafe") # search : 与えられた文字列の中で一致しているのが存在しているか確認
print_match(o)
lst = p.findall("careless good care cafecafefe") # findall : 一致する全てをリスト形式でリターン
print(lst)

# 1. p = re.compile("求めている携帯")
# 2. n = p.match("比較対象の文字列") : 与えられた文字列の最初から一致しているか確認
# 3. n = p.search("比較対象の文字列") : 与えられた文字列の中で一致しているのが存在しているか確認
# 4. lst = p.findall("比較対象の文字列") : 一致する全てをリスト形式でリターン
