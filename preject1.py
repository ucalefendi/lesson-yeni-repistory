import requests
import json


gelen_cevap = requests.get("http://api.open-notify.org/astros.json")
uzaydaki_insan_sayisi1 = gelen_cevap.json()["number"]
# uzaydaki_insan_sayisi2 = gelen_cevap.json()["message"]

# print(uzaydaki_insan_sayisi1)


for kisi in gelen_cevap.json()["people"]:
    print(kisi['name'],kisi['craft'])




