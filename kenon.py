import os
import datetime
import requests
from bs4 import BeautifulSoup

try:
    import settings as st
except ModuleNotFoundError:
    import sample_settings as st
    st.payload['login']['username'] = os.environ['USERNAME']
    st.payload['login']['password'] = os.environ['PASSWORD']


def login(session):
    return session.post(st.url['login'], st.payload['login'], headers=st.headers)


def getTodayId(session):
    res = session.get(st.url['date_list'], headers=st.headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    dt_now_jst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

    # today = datetime.date.today()
    today = dt_now_jst.today()
    keyword = '{}/{}検温'.format(today.month, today.day)

    for e in soup.find_all(class_='activityinstance')[1:]:
        if keyword in e.find('span').text:
            return e.find('a').get('href').split('=')[-1]
    return None


def hasSubmitted(session, idx):
    res = ss.get(st.url['input']+idx, headers=st.headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.find('input').get('value') == '続ける'


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

        kenon_id = getTodayId(ss)

        #if not hasSubmitted(ss, kenon_id):
        if True:
            kenon_submit(ss, kenon_id)
            print('Submitted.')

