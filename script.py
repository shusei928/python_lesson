from bs4 import BeautifulSoup
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}

# url_address = "https://www.homes.co.jp/chintai/tokyo/list/?cond%5Broseneki%5D%5B88205061%5D=88205061&cond%5Bmonthmoneyroomh%5D=0&cond%5Bhousearea%5D=0&cond%5Bhouseageh%5D=0&cond%5Bwalkminutesh%5D=0&bukken_attr%5Bcategory%5D=chintai&bukken_attr%5Bpref%5D=13"
url_address = "https://www.tokyodisneyresort.jp/tdl/restaurant/detail/317/"
session = requests.Session()
html = session.get(url_address, headers=headers)
# html = requests.get(url_address)
soup = BeautifulSoup(html.text, "html.parser")
# print(soup)

# text = soup.find("li")
# print(text)

# proxies_dic = {
#   "http": "http://proxy.example.co.jp:8080",
#   "https": "http://proxy.example.co.jp:8080",
# }
# r = requests.get("https://www.kantei.go.jp", proxies=proxies_dic)


# print(r.status_code)
for table in soup.findAll(class_="link"):
    for sub in table.findAll("li"):
        for parts in sub.findAll("a"):
            text = re.sub(r"^\s+|\s+$", "", parts.text)
            link = parts.get("href")
            link = "https://www.tokyodisneyresort.jp/" + link
            print(text + ":")
            print(link)

