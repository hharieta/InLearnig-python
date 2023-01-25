import requests
import os
import json


def main():
    username = os.getlogin()
    url = "https://webhook.site/1f9a83d4-3cbe-49ae-a586-3641b3ef4001"
    file = open("orden.json", "r")
    payload = json.load(file)
    query_params = {"username": username}

    response = requests.post(url, data=payload, params=query_params)

    print(response.status_code)


if __name__ == '__main__':
    main()
