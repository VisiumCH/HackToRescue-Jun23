import openai
import time

from utils import scrape_google, extract_content, generate_question_message, generate_text
from constants import OPEN_AI_KEY

def main():
    """Main function."""
    OPENAI_MODEL_NAME = "gpt-3.5-turbo"
    # Statement that we want to analyse
    statement = """Autism MMS Miracle mineral solutions."""
    # Text that is added to the prompt
    #TODO: improve it
    prompt_text = generate_text()

    # Retrieve top 3 urls found in Google
    urls = scrape_google(statement)[:5]
    url = urls[0]
    content = extract_content(url)

    message = generate_question_message(content, url, prompt_text)
    openai.api_key = OPEN_AI_KEY
    try:
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL_NAME,
            messages=message,
            n=1,
            max_tokens=1000,
        )
        time.sleep(2)

    except Exception as e:
        print("Response not retrieved")

    print(response["choices"][0]["message"]["content"], sep="\n")



if __name__ == "__main__":
    main()