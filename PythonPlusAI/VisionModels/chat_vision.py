'''

in order to read an image
instead of sending a string in the "content" field,
we send a list of dictionaries, one representing text,
and one representing an image URL.

'''

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
endpoint = os.getenv("ENDPOINT")
model = os.getenv("MODEL")

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": [
                {
                  "text": "Is this a unicorn?", 
                  "type": "text"
                },
                {
                  "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Ur-painting.jpg"
                    },
                  "type": "image_url",
                },
            ],
        }
    ],
    temperature=0.5,
    #top_p=1,
    model=model
)

print(response.choices[0].message.content)