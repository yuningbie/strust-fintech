#!/usr/bin/python3

import sys
import json
import requests

print("testst")
baseUrl = "https://xchain.io"
asset = "btc"
response = requests.get(baseUrl + "/api/asset/" + asset)
print(response.status_code)
print(response.json())