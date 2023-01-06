'''
Retrieves market news, however, the number of URLs are sometimes
limitation to one and that site might require bot check
'''
import requests
from mySecrets import getYahooApiHost, geRapidApiKey
from utility.webScraping import getRawData

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"

querystring = {
    "uuid":"9803606d-a324-3864-83a8-2bd621e6ccbd",
    "region":"US"}

headers = {
	"X-RapidAPI-Key": geRapidApiKey(),
	"X-RapidAPI-Host": getYahooApiHost()
}

#returns the json response from RapidAPI for Yahoo's finance news
def getYahooFinance():
    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonRes = response.json()
    return jsonRes

#extracts a list of URLs from the json response of Yahoo Finance
def urlList(jsonRes):
    news_url_list = []
    data = jsonRes["data"]
    contents = data["contents"]
    for item in contents:
        content = item["content"]
        canonicalUrl = content["canonicalUrl"]
        url = canonicalUrl["url"]
        news_url_list.append(url)
    return news_url_list  

def summaryList(jsonRes):
    summary = []
    data = jsonRes["data"]
    contents = data["contents"]
    for item in contents:
        content = item["content"]
        summary.append(content["summary"])
    return summary

#returns the raw string from all the URLs provided by getYahooFinance
def getFinanceRawNews():
    jsonRes = getYahooFinance()
    news_url_list = urlList(jsonRes)
    data_list = getRawData(news_url_list)
    summary_list = summaryList(jsonRes)
    return data_list + summary_list

#print(getFinanceRawNews())

