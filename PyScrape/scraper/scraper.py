import requests
from bs4 import BeautifulSoup
import random

def get_random_user_agent():
    """
    Returns a random user agent string from a predefined list to mimic different browsers.
    This can help bypass some basic web scraping protections by making each request appear
    to come from a different browser.
    
    Returns:
        str: A random user agent string.
    """
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    ]
    return random.choice(user_agents)

def scrape_website_generalized(url):
    """
    Enhanced web scraper that extracts titles, headers, list items, and hyperlinks from a given URL.
    It showcases features like dynamic user-agent spoofing, comprehensive error handling, and selective data extraction.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        None
    """
    
    # Using the dynamic user-agent
    headers = {'User-Agent': get_random_user_agent()}

    try:
        # Making a GET request to the website, including the dynamic headers.
        response = requests.get(url, headers=headers)
        
        # Checking for HTTP errors and raising an exception for 4xx and 5xx status codes.
        response.raise_for_status()
        
        # Parsing the HTML content of the page with BeautifulSoup.
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extracting and printing the page title
        print(f"\nPage Title: {soup.title.string if soup.title else 'No title found'}")
        
        # Extracting and printing headers (h2 tags)
        print("\nHeaders (h2 tags):")
        headers = soup.find_all('h2')
        for header in headers:
            print(header.text.strip())

        # Extracting and printing list items (li tags)
        print("\nList Items (li tags):")
        list_items = soup.find_all('li')
        for item in list_items:
            print(item.text.strip())

        # Extracting and printing all hyperlinks
        print("\nHyperlinks:")
        links = soup.find_all('a')
        for link in links:
            print(f"{link.text.strip()}: {link.get('href')}")
    
    except requests.exceptions.RequestException as e:  # This catches all request-related errors
        print(f'Request error occurred: {e}')
    except Exception as err:  # General catch-all for any other exceptions
        print(f'An unexpected error occurred: {err}')

if __name__ == "__main__":
    # Replace 'https://example.com' with the actual URL you wish to scrape.
    url = 'https://example.com'
    scrape_website_generalized(url)
