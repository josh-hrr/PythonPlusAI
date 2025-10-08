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

messages = [
    {
      "role": "system",
      "content": "You are a useful assistance that makes lots of cat puns.",
    },
]

while True:
    question = input("\nYour questions: ")
    print("sending question...")

    messages.append(
       {
          "role": "user",
          "content": question,
       }
    )
    response = client.chat.completions.create(
       model=model,
        messages=messages,
        temperature=0.5,
        #stream=True
    ) 
    bot_response = response.choices[0].message.content
    messages.append(
        {
            "role": "assistant",
            "content": bot_response,
        }
    )
    print(f'Anaswer: ')
    print(bot_response)