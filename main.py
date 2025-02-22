import requests
from bs4 import BeautifulSoup
import time
from utils import extract_urls


def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    for i in url:
        try:
            response = requests.get(i, headers=headers, timeout=10)
            response.raise_for_status(); # Watch out for bad responses (4XX, 5XX)
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {i}: {e}")
            return None
    
def parse_headlines(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')

    # Assuming headlines are in h2 tags:
    headlines = soup.find_all('h2')
    matches = []
    for h in headlines:
        text = h.get_text()
        if keyword.lower() in text.lower():
            a_tag = h.find('a')
            link = a_tag['href'] if a_tag and 'href' in a_tag.attrs else None
            matches.append((text.strip(), link))
    return matches
    

def main():
    url = extract_urls('websites.txt');
    keyword = 'to'
    
    while True:
        html = fetch_page(url)
        if html:
            results = parse_headlines(html, keyword)
            if results:
                print(f"Found {len(results)} articles containing '{keyword}':")
                for headline, link in results:
                    print(f"Headline: {headline}")
                    if link:
                        print(f"Link: {link}")
                    print('-' * 40)
            else:
                print(f"No results found containing '{keyword}' on {url}")
        else:
            print("Failed to retrieve page content.")
        time.sleep(600)

if __name__ == '__main__':
    main()