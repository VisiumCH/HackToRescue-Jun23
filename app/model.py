import time
import json
import openai
from constants import OPEN_AI_KEY
from utils import scrape_google, extract_content, generate_question_message, generate_text

OPENAI_MODEL_NAME = "gpt-3.5-turbo"
openai.api_key = OPEN_AI_KEY

class ChatGPTModel:
    def __init__(self) -> None:
        pass

    def predict(self, inputs_: str):
        statement = """Autism MMS Miracle mineral solutions."""
        # Text that provides
        text = generate_text()

        # Retrieve top 3 urls found in Google
        urls = scrape_google(inputs_)[:5]
        outputs = []
        for url in urls:
            content = extract_content(url)
            message = generate_question_message(content, url, text)
            try:
                response = openai.ChatCompletion.create(
                    model=OPENAI_MODEL_NAME,
                    messages=message,
                    n=1,
                    max_tokens=500,
                )
                data = response["choices"][0]["message"]["content"]
                meta = json.loads(data)
                meta["link"] = url
                outputs.append(meta)
            except:
                pass
        return outputs