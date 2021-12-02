from bs4 import BeautifulSoup
import requests
import re
import csv
import regex

shop_list = []
url_list = []

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}

# url_address = "https://www.homes.co.jp/chintai/tokyo/list/?cond%5Broseneki%5D%5B88205061%5D=88205061&cond%5Bmonthmoneyroomh%5D=0&cond%5Bhousearea%5D=0&cond%5Bhouseageh%5D=0&cond%5Bwalkminutesh%5D=0&bukken_attr%5Bcategory%5D=chintai&bukken_attr%5Bpref%5D=13"
url_address = "https://www.tokyodisneyresort.jp/tdl/restaurant.html"

session = requests.Session()
html = session.get(url_address, headers=headers)
soup = BeautifulSoup(html.text, "html.parser")

for table in soup.findAll(class_="section-list"):

    # 店名の取得
    for sub in table.findAll(class_="heading3"):
        shop_name = re.sub(r"^\s+|\s+$", "", sub.text)

        # リストに追加
        shop_list.append(shop_name)

    # URLの取得
    for sub in table.findAll(class_="button"):
        for parts in sub.findAll("a"):
            if regex.findall("店舗メニュー",parts.text):
                
                url = parts.get("href")
                url = "https://www.tokyodisneyresort.jp/" + url

                # リストに追加
                url_list.append(url)

all_list = list(zip(
    shop_list,
    url_list,
))


# csvファイル作成
header = ['店名', 'URL']
body = all_list
with open('sample.csv', 'w', newline='', encoding="Shift_jis") as f: # 書き込みモードでファイルを開く
  csv_writer = csv.writer(f)
  csv_writer.writerow(header)
  csv_writer.writerows(body)
f.close()