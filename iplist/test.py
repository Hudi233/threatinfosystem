import requests
import json
post_data = json.dumps({"ip":"xxx","memberID":"xxx","uri":"xxx"})
info = requests.post("http://xxx", data = post_data, headers={'Content-Type': 'application/json'})
print(info.text)
