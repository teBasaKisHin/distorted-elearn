import json
import requests as req
from bs4 import BeautifulSoup


def main():
    with open("inputData.json", "r") as f:
        data = json.load(f)
    
    with req.Session() as ses:
        res = ses.post(data["url"]["login"], headers=data["header"], data=data["login"])
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        data["session"]["sesskey"] = soup.find("input", attrs={"name":"sesskey"}).get("value")
        data["message"].update(data["session"]) # or data["message"]["sesskey"] = data["session"]["sesskey"]

        while True:
            msg=str(input("Your message ('q'exits) :"))
            if msg == "q":
                ses.get(data["url"]["logout"], headers=data["header"], params=data["session"])
                print("this app is finished")
                break
            data["message"]["message"] = msg
            res = ses.post(data["url"]["message"], headers=data["header"], data=data["message"])
            res.raise_for_status()
            print("Message sent")


if __name__ == '__main__':
    main()

