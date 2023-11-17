import requests
import os

def add_item(title):

    reqUrl = "https://trello-proxy.azure-api.net/1/cards"

    query_params = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TODO_LIST_ID"),
        "name": title
    }

    response = requests.post(reqUrl, params = query_params)

    print(response.text)


def get_items():
    board_id = os.getenv("TRELLO_BOARD_ID")

    reqUrl = f"https://trello-proxy.azure-api.net/1/boards/{board_id}/lists"

    query_params = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "cards": "open"
    }

    response = requests.get(reqUrl, params = query_params)

    response.raise_for_status()

    response_list = response.json()

    items = []

    for trello_list in response_list:
        for trello_card in trello_list['cards']:
            trello_card['status'] = trello_list['name']
            items.append(trello_card)

    return items