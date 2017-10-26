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
	
	while 1:
		mesg = input("message(exit is \"q\"): ")
		if (mesg == 'q'):
			break
	
		getter = int(input("Who to send?(number)"))
		while 1:
			if (getter <= 41) and (getter > 0):
				break
			else:
				getter = int(input("Who to send?(number)"))
	
		j["message"]["message"] = mesg
		j["message"]["id"] = str(getter + 211) 
	
		e = ses.post(j["url"]["message"],headers = j["headers"],data = j["message"])

	e = ses.get(j["url"]["logout"],headers = j["headers"],params = j["logout"])
