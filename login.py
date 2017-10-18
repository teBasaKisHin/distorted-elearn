import requests as req
import json

with open("personalInfo.json", "r") as f:
    data = json.load(f)

with open("url.json", "r") as f:
    url = json.load(f)

ses = req.Session()
res = ses.post(url["login"], data=data)
print(res.text)

