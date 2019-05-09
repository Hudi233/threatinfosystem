import requests
import json
post_data = json.dumps({"ip":"100.73.49.130","memberID":"717598943303818513","uri":"/mybankv21/phptradeui/credit/indexToast"})
info = requests.post("http://100.109.70.44:8000/threatinfo/search/", data = post_data, headers={'Content-Type': 'application/json'})
print(info.text)
