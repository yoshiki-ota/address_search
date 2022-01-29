import requests

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=0250067"

response = requests.get(url)
print(response.text)
