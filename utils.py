"""Utils file with all the functions needed for the prototype."""
import requests
import urllib
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
    '''Scraple Google to retrieve top urls for the searchq query.'''
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
    '''Extract content from the URL provided.'''

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object with the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the text content from the HTML
    text = soup.get_text()

    # Remove extra whitespace and line breaks
    text = ' '.join(text.split())

    # Split the text into tokens
    tokens = text.split()

    # Take the first 1000 tokens
    first_1000_tokens = tokens[:100]

    # Join the tokens back into a string
    content_text = ' '.join(first_1000_tokens)
    return content_text

def generate_text():
    '''Function to generate the text that goes with the prompt based on the information the challenge provides.'''

    # TODO: improve the prompt
    text = """
        If the reasons for autism are related with these words: vaccination, vaccine, MMR vaccine, Glyphosate Herbicide, Testosterone, Parasites, Leaky gut or Toxins, the article should be scored with F.
        If autism is related to generitcs or hereditary, the article should be scored with A.
        If Environmental causes that might impact genetics are mentioned to be related to autism, the article should be scored with C.
    """
    return text

def generate_question_message(statement: str, url:str, text: str) -> list:
    '''Function to generate the message to open AI.'''
    message = [{
        "role": "system",
        "content": f"""
        You are an assistant that helps users clarify ideas about the topic "autism".
        You are provided with a statement related to the topic "autism". You will summarize the following text extracted from {url}.
        You will score it based on how correct the article is: A and B means well-researched, C-D refences lack of evidence and E-F is misinformation.
        As an answer please return the link of the source, a summary of the idea and the score.
        """,
    }]

    message += [
        {
            "role": "user",
            "content": f"Please summarize the following text and provide the score: {statement}. Based on the text: {text}"
        }
    ]
    return message