'''
- Data
	- decide sources
	- choose categories for news such as us, eu, uk, middle east, china
	- stock market should have its own categories
	- provide a means to input text manually and have it summarized
- Data Cleansing
- Social consensus
- OpenAI
- HTML page for the prints
- Auto publish to the blog
- Execution scheduler
- Exception handling


next:
	- get the res from rapid API in pages, so you can submit separate paragraphs to OpenAI
	- query rapid API for categories: politics, market, technology
'''
#below effort is to be able to read from parent dir
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from data.bingNews import getPoliticsRawNews
from data.yahooFinanceNews import getFinanceRawNews
from openAI.summarize import getSummary2, getSummary
from utility.cleanseData import cleanseData
from publish.googleBlogger import getBlog

'''
#test case: bing returns a list of news but openAI doesn't summarize them well
data = getPoliticsRawNews() #getFinanceRawNews()
summarized_data = getSummary(data)
summarized_data = cleanseData(summarized_data)
print(summarized_data)
'''

'''
#no need to summarize the news from finance as it retrieves a summary from the API
data = getFinanceRawNews()
print(data[0])
'''

print(type(getBlog()))