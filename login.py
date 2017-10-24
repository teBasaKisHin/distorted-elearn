import json
import requests as req
from bs4 import BeautifulSoup


def main():
    with open("inputData.json", "r") as f:
        data = json.load(f)
    
    ses = req.Session()
    res = ses.post(data["url"]["login"], headers=data["header"], data=data["login"])
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    data["message"]["sesskey"]=soup.find("input", attrs={"name":"sesskey"}).get("value")

    while True:
        msg=str(input("Your message ('q'exits) :"))
        if msg == "q":
            break
        data["message"]["message"]=msg
        res = ses.post(data["url"]["message"], headers=data["header"], data=data["message"])
        res.raise_for_status()
        print("Message sent")

    print("This app is finished")

if __name__ == '__main__':
    main()

