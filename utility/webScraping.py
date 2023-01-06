import requests
from bs4 import BeautifulSoup


from utility.cleanseData import cleanseData

def getSoupText(url):
    response = requests.get(url)
    if response.status_code != 200:
        return ""
    soup = BeautifulSoup(response.content, 'html.parser')
    return(soup.get_text())

#visits each URL and collects the soup.text in a raw string
def getRawData(news_url_list):
    data = []
    for url in news_url_list:
        news = getSoupText(url)
        if len(news) > 0:
            data.append(cleanseData(news))
    return data