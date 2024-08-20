import requests
from bs4 import BeautifulSoup

def fetch_and_save_links(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        links = {a['href'] for a in soup.find_all('a', href=True)}

        with open(filename, 'w') as file:
            for link in links:
                file.write(link + '\n')

        print(f"Links have been saved to {filename}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the webpage to scrape: ")
    fetch_and_save_links(url, 'links.txt')