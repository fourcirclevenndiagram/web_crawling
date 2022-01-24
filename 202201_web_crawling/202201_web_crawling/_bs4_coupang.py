import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=razer+%ED%82%A4%EB%B3%B4%EB%93%9C+%ED%9D%91%EC%B6%95&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text() # 製品名
    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 値段
    rate = item.find("em", attrs={"class":"rating"}) # 評価点数
    if rate:
        rate = rate.get_text()
    else:
        rate = "評価点数なし"

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 評価点数の数
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        rate_cnt = "評価点数の数なし"

    print(name, price, rate, rate_cnt)


