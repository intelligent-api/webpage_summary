import bs4, requests
import base64
import http.client
import json
from dotenv import load_dotenv
import os
import sys

from models.api_response import APIResponse

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if len(sys.argv) == 1:
    print(
        "You must pass in the URL of the webpage to summarize, e.g. python main.py https://docs.intelligent-api.com/docs/introduction"
    )
    exit(1)

response = requests.get(
    sys.argv[1],
    headers={"User-Agent": "Mozilla/5.0"},
)
soup = bs4.BeautifulSoup(response.text, features="html.parser").text

# basic configuration
client_id = CLIENT_ID
client_secret = CLIENT_SECRET

# create a base64 encoded api key
api_key_bytes = base64.b64encode((client_id + ":" + client_secret).encode("utf-8"))
api_key = api_key_bytes.decode("utf-8")

# use the api key as a basic token
authorization = "Basic " + api_key

# populate endpoint parameters
text = soup
user_agent = "Intelligent API Sample Python Code"

data = {"text": text}

json_data = json.dumps(data)

# invoke the API endpoint
host = "api.intelligent-api.com"
path = "/v1/text/summarize"

connection = http.client.HTTPSConnection(host)

headers = {
    "Authorization": authorization,
    "Content-Type": "application/json",
    "User-Agent": user_agent,
}

connection.request("POST", path, body=json_data, headers=headers)
response = connection.getresponse()
response_data = response.read().decode("utf-8")

json_data = json.loads(response_data)
api_response = APIResponse(**json_data)

print("The summary of the webpage:")

for x in api_response.summaryPoints:
    print(f"- {x}")

connection.close()
