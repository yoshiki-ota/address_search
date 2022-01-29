import requests


def main():
    pass


zipcode = "0250067"
# zipcode = input("郵便番号<ハイフン無し7桁>は?")   # 郵便番号<ハイフン無し7桁>は?

url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

response = requests.get(url)
pref_name = response.json()['results'][0]['address1']
city_name = response.json()['results'][0]['address2']
town_name = response.json()['results'][0]['address3']

address = f"{pref_name}{city_name}{town_name}"
print(address)

if __name__ == '__main__':
    main()
