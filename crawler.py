import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

urls = [
    'https://quotes.toscrape.com/',
    'https://books.toscrape.com/'
]
keywords = ['book', 'to', 'try', 'login']

visited = set()

def crawl(url, depth=2):
    if depth == 0 or url in visited:
        return
    
    visited.add(url)

    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch URL {url}: {e}")
        return

    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a', href=True):
        absolute_url = urljoin(url, link['href'])
        if absolute_url.startswith(url) and absolute_url not in visited:
            crawl(absolute_url, depth - 1)
            # Recursive crawl, baby

for url in urls:
    crawl(url, depth=2)

print(visited)



