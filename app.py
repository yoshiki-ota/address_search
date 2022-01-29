import requests

zipcode = "0250067"
# zipcode = input("郵便番号<ハイフンなし7桁>は？:")
url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

response = requests.get(url)
print(response.text)
