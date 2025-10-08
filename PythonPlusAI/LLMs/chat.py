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
    messages=[
        {
            "role": "system",
            "content": "You are a teacher for kids",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    temperature=0.5,
    #top_p=1,
    model=model
)

print(response.choices[0].message.content)