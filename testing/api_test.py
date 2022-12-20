import requests
import urllib.parse
import base64
import json


url = "https://api.roadgoat.com/api/v2/destinations/rijeka-croatia"


encoded_bytes = base64.b64encode('ba673fe35348681b558314fb690b18a4:53ff80aa7bddfa4370a99e6b77905636'.encode("utf-8"))
auth_key = str(encoded_bytes, "utf-8")
headers = {
  'Authorization': f'Basic {auth_key}'
}
response = requests.get(url, headers=headers)

a = response.json()


with open('data.json', 'w') as f:
    json.dump(a, f)

