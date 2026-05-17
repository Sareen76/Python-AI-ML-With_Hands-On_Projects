'''
    WebScraping using MultiThreading
    WebScraping is a technique used to extract data from websites. It involves making HTTP requests to web pages, parsing the HTML content, and extracting the desired information. MultiThreading can significantly speed up the web scraping process by allowing multiple requests to be made concurrently.
'''



import threading
import requests
from bs4 import BeautifulSoup
import time


urls = ['https://docs.langchain.com/oss/python/langchain/overview',
'https://docs.langchain.com/oss/python/langchain/install',
'https://docs.langchain.com/oss/python/langchain/quickstart']


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
    # print(soup.text[:200])  # Print first 200 characters of the content

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Web Scraping Completed")

