import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')

APIKEY = os.getenv("APIKEY")


API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept": "image/png",
	"Authorization": APIKEY,
	"Content-Type": "application/json"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
