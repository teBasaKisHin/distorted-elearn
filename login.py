import requests as req
import json

def main():
    with open("inputData.json", "r") as f:
        data = json.load(f)

    ses = req.Session()
    res = ses.post(data["url"]["login"], data=data["login"])
    print(res.text)


if __name__ == '__main__':
    main()

