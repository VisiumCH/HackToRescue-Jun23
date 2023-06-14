"""Utils file with all the functions needed for the prototype."""
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def get_source(url):
    """Return the source code for the provided URL.

    Args:
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html.
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.',
                      'https://translate.google.com/')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

def extract_content(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object with the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the main content element on the page (you may need to inspect the HTML to identify the appropriate element)
    content_element = soup.find('div', class_='content')  # Replace 'div' and 'class_' with the actual HTML tag and class of the content element
    print(content_element)
    # Extract the text from the content element
    content_text = content_element.get_text() if content_element else soup.get_text()
    print(content_text)
    return content_text

def generate_text():
    '''Function to generate the text that goes with the prompt based on the information the challenge provides.'''
    # TODO: get the text from the webpage
    NotImplementedError
    return None

def generate_question_message(statement: str, text: str) -> list:
    NotImplementedError