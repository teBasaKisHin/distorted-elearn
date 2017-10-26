import requests as req
import json
import identify

def send():
	with open("inputData.json","r") as f:
		j = json.load(f)

	ses = req.Session()
	e = ses.post(j["url"]["login"],headers = j["headers"],data = j["login"])	
	j["message"]["sesskey"] = identify.sessGet(e.text)	
	j["logout"]["sesskey"] = j["message"]["sesskey"]	
	mesg = input("message : ")
	
	getter = 0
	while 1:
		if getter > 41 or getter < 1:
			getter = int(input("Who to send?(number)"))
		else:
			break
	
	j["message"]["message"] = mesg
	j["message"]["id"] = str(getter + 211) 
	j["message"]["sesskey"] = identify.sessGet(e.text)
	
	e = ses.post(j["url"]["message"],headers = j["headers"],data = j["message"])

	e = ses.get(j["url"]["logout"],headers = j["headers"],params = j["logout"])
