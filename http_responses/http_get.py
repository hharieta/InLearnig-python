import requests

def main():
    response = requests.get(
        "https://api.github.com/search/repositories",
        params={"q": "portafolio_SOs"}
        )
    print(response.json())
    data = response.json()
    print(data["items"][4]["full_name"])


if __name__ == '__main__':
    main()
