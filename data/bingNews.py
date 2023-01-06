'''
This module uses Bing news from RapidAPI. 
There are two main functions: getTechRawNews and getPoliticsRawNews.
These functions will retrieve raw text from all the news URLs that are
provided by RapidAPI's response
'''

import requests
from mySecrets import getBingApiHost, geRapidApiKey
from utility.webScraping import getRawData

url = "https://bing-news-search1.p.rapidapi.com/news"

querystring_politics = {
	"safeSearch":"Off",
	"textFormat":"Raw",
	"setLang": "En",
	"count": "100",
	"category": "politics"
	}

querystring_tech = {
	"safeSearch":"Off",
	"textFormat":"Raw",
	"setLang": "En",
	"count": "100",
	"category": "Technology"
	}
			
headers = {
	"X-BingApis-SDK": "true",
	"X-RapidAPI-Key": geRapidApiKey(),
	"X-RapidAPI-Host": getBingApiHost()
	}	

#returns the json response from RapidAPI for Bing's political news
def getBingApiPolitics():
	response = requests.request("GET", url, headers=headers, params=querystring_politics)
	jsonRes = response.json()
	return jsonRes

#returns the json response from RapidAPI for Bing's science & tech news
def getBingApiTech():
	response = requests.request("GET", url, headers=headers, params=querystring_tech)
	jsonRes = response.json()
	return jsonRes	

#extracts a list of URLs from the json response of Bing's news
def urlList(jsonRes):
	news_url_list = []
	for news in jsonRes["value"]:
		news_url_list.append(news["url"])
	return news_url_list

#returns the raw string from all the URLs provided by getBingApiPolitics
def getPoliticsRawNews():
	jsonRes = getBingApiPolitics()
	news_url_list = urlList(jsonRes)
	data_list = getRawData(news_url_list)
	return data_list

#returns the raw string from all the URLs provided by getBingApiTech
def getTechRawNews():
	jsonRes = getBingApiTech()
	news_url_list = urlList(jsonRes)
	data_list = getRawData(news_url_list)
	return data_list	

#test
#print(getPoliticsRawNews())

