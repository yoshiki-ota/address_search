import requests

zipcode = "0250067"
# zipcode = input("郵便番号<ハイフンなし7桁>は？:")
url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

response = requests.get(url)

# jsonでdicに変換した↓
results = response.json()['results']

pref_name = (results[0]['address1'])
city_name = (results[0]['address2'])
town_name = (results[0]['address3'])

address = f"{pref_name}{city_name}{town_name}"
print(address)
