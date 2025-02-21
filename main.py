import requests
from bs4 import BeautifulSoup
import time

def fetch_page(url):
    headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

def main():
    r = requests.get('https://quotes.toscrape.com/')
    print(r)
    print(r.content)

main()