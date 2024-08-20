import requests

websites = ['https://google.com', 'https://easdasdasdasdasdxawaswedwdwewwmple.com']

for website in websites:
    try:
        response = requests.get(website)
        if response.status_code == 200:
            print(f"Available: {website}")
    except requests.exceptions.ConnectionError:
        print(f"Domain not found: {website}")