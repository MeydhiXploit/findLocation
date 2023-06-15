import requests
import json
import cowsay

cowsay.cow("MeydhiXploit")
print("-" * 40)
ipaddress = input("Input Your IP Address: ")
iprequests = requests.get(f"http://ip-api.com/json/{ipaddress}")
if iprequests.status_code == 200:
    ipdata = json.loads(iprequests.text)
    if ipdata["status"] == "success":
        print("Ip address:", ipaddress)
        print("Query:", ipdata["query"])
        print("Country:", ipdata["country"])
        print("Country Code:", ipdata["countryCode"])
        print("City:", ipdata["city"])
        print("Timezone:", ipdata["timezone"])
        print("Region:", ipdata["region"])
        print("Region name:", ipdata["regionName"])
        lat = ipdata["lat"]
        lon = ipdata["lon"]
        print("Location :",lat,",",lon)
        maps = f"https://www.google.com/maps/@{lat},{lon},9z?hl=id"
        print("Maps :",maps)
        print("Status:", ipdata["status"])
        print("-" * 40)
    else:
        print("Failed to retrieve IP information.")
