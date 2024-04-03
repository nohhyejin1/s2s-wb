# client.py

import requests
import json

url = "https://be.rosieshop.domain.aws-team-demo.link/add/cart"

req = {
    "user_id": "nhj",
    "item_id": "item2"
}

response = requests.post(url,
                         data=json.dumps(req),
                         headers={"Content-Type": "application/json"},
                         verify=False)

print(response.text)
