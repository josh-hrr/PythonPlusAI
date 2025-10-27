'''

Graph analysis can be used to determine an specific outcome.
Based on an image provided.

'''

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")

client = OpenAI(
  base_url=base_url,
  api_key=token
)

message = [
  {
    "role": "user",
    "content": [
      {
        "text": "What zone are we losing the most trees in?",
        "type": "text"
      },
      {
        "image_url": {
          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/20210331_Global_tree_cover_loss_-_World_Resources_Institute.svg/1280px-20210331_Global_tree_cover_loss_-_World_Resources_Institute.svg.png"
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
