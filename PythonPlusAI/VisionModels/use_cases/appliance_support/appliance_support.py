'''

analizing a table that contains prices to extract the most expensive one.

'''

import os 
from dotenv import load_dotenv
from openai import OpenAI
import base64

load_dotenv()
base_url = os.getenv("BASE_URL")
token = os.getenv("GITHUB_TOKEN")
model = os.getenv("MODEL")

def convert_into_base64(path):
  with open(path, "rb") as file:
    file_content = file.read()
    image_encode = base64.b64encode(file_content).decode("utf-8")
  return f"data:image/png;base64,{image_encode}" 

client = OpenAI(
  base_url=base_url,
  api_key=token
)

message = [
  {
    "role": "user",
    "content": [
      {
        "text": "How do I set this to wash the dishes quickly?",
        "type": "text"
      },
      {
        "image_url": {
          "url": convert_into_base64("img/dishwasher.png")
        },
        "type": "image_url"
      }
    ]
  }
]

response = client.chat.completions.create(
  messages=message,
  model=model,
  temperature=0.5
)

print(response.choices[0].message.content)