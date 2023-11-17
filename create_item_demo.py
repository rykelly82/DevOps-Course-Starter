import requests
import dotenv
import os

dotenv.load_dotenv()

reqUrl = "https://trello-proxy.azure-api.net/1/cards"

query_params = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "idList": os.getenv("TODO_LIST_ID"),
    "name": "Walk the dog"
}

response = requests.post(reqUrl, params = query_params)

print(response.text)