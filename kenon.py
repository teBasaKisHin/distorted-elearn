import datetime
import requests
from bs4 import BeautifulSoup

import settings as st



def login(session):
    return session.post(st.url['login'], st.payload['login'], headers=st.headers)


def getIdof(session, keyword):
    res = session.get(st.url['date_list'], headers=st.headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    for e in soup.find_all(class_='activityinstance')[1:]:
        if keyword in e.find('span').text:
            return e.find('a').get('href').split('=')[-1]
    return None


def kenon_submit(session, idx):
    pass


if __name__ == '__main__':
    with requests.Session() as ss:
        res = login(ss)
        
        today = datetime.date.today()
        keyword = '{}/{}検温'.format(today.month, today.day)
        kenon_id = getIdof(ss, keyword)
        print(kenon_id)

        kenon_submit(session, kenon_id)

