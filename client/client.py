# client.py

import requests
import json

url = "http://localhost:8000/add/cart"

req = {
    "user_id": "nhj",
    "item_id": "item2"
}

response = requests.post(url,
                         data=json.dumps(req),
                         headers={"Content-Type": "application/json"})

print(response.text)