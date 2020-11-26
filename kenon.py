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
    res = session.get(st.url['input']+idx, headers=st.headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    payload = dict()

    for e in soup.find_all('select'):
        payload[e.get('name')] = '1'

    for e in soup.find_all('input'):
        payload[e.get('name')] = e.get('value')
    
    return session.post(st.url['submit'], payload, headers=st.headers)


if __name__ == '__main__':
    with requests.Session() as ss:
        login(ss)
        
        today = datetime.date.today()
        keyword = '{}/{}検温'.format(today.month, today.day)
        kenon_id = getIdof(ss, keyword)

        if kenon_id is not None:
            res = kenon_submit(ss, kenon_id)
            print('Submitted.')

