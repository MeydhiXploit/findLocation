import requests
import json
import cowsay
cowsay.cow("Meydhi Ari Nugroho")
ipaddress = input("Input Your IP Address: ")
iprequests = requests.get(f"http://ip-api.com/json/{ipaddress}")

if iprequests.status_code == 200:
    ipdata = iprequests.json()
    if ipdata["status"] == "success":
        print("Ip address:", ipaddress)
        print("Query:", ipdata["query"])
        print("Country:", ipdata["country"])
        print("Country Code:", ipdata["countryCode"])
        print("City:", ipdata["city"])
        print("Timezone:", ipdata["timezone"])
        print("Status:", ipdata["status"])
        print("Region:", ipdata["region"])
        print("Region name:", ipdata["regionName"])
        print("Lat :",ipdata["lat"])
        print("Lon :",ipdata["lon"])
    else:
        print("Failed to retrieve IP information.")
else:
    print("Failed to connect to IP API.")
