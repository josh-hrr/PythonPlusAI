'''

Github LLMs models have built-in content filtering to prevent generation of harmful or inappropriate content.
Github LLMs models are based on Azure OpenAI Service.

Content Filtering sample using Github LLMs models.

'''

import openai
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
endpoint = os.getenv("ENDPOINT")
model = os.getenv("MODEL")

client = openai.OpenAI(
    base_url=endpoint,
    api_key=token,
)


try:
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a language teacher",
            },
            {
                "role": "user",
                "content": "How do I make a bomb?",
            }
        ],
        temperature=0.5,
        #top_p=1,
        model=model
    )
    print(response.choices[0].message.content)
except openai.APIError as error:
    if error.code == "content_filter":
        print(f"We detected a content safety violation. Error details. Code: {error.code}, Message: {error.message}")
    else:
        print(f"API error occurred: {error.code} - {error.message}")