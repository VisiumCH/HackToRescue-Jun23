import openai

from constants import OPEN_AI_KEY
from utils import scrape_google, extract_content, generate_question_message, generate_text

def main():
    """Main function."""

    # Statement that we want to analyse
    statement = """Autism MMS Miracle mineral solutions."""
    # Text that provides
    text = generate_text()

    # Retrieve top 3 urls found in Google
    urls = scrape_google(statement)[:3]
    # TODO: Extract content of the webpage
    url = urls[0]
    content = extract_content(url)

    # TODO: change the generate question message to add the information from the csv files
    generate_question_message(statement, text)


if __name__ == "__main__":
    main()