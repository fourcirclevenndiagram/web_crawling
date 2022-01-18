import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print("soup.a       : ", soup.a)
print("soup.a.attrs : ", soup.a.attrs)
print(soup.a["href"])

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
print(soup.find(attrs={"class":"Nbtn_upload"}))

print("liタグの情報採取")
print(soup.find("li", attrs={"class":"rank01"}))
rank01 = soup.find("li", attrs={"class":"rank01"})
print(rank01.a)
print(rank01.a.get_text())
# print(rank01.next_sibling)   # このsiblingに該当する情報は単なる改行情報なのか、なにも表示されない
print(rank01.next_sibling.next_sibling)
rank02 = rank01.next_sibling.next_sibling
rank03 = rank02.next_sibling.next_sibling
print(rank03.a.get_text())

print(rank01.parent)
rank02 = rank01.find_next_sibling("li")
print(rank02.a.get_text())
rank03 = rank02.find_next_sibling("li")
print(rank03.a.get_text())

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.get_text())