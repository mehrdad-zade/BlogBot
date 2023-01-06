import requests
from apiclient.discovery import build #pip install --upgrade google-api-python-client
from mySecrets import getBloggerApiKey, getBloggerId

def getBlog():
    blog = build('blogger', 'v3', developerKey=getBloggerApiKey())
    return blog

