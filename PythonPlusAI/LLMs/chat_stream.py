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
            "content": "You are a useful assistance that makes lots of cat puns.",
        },
        {
            "role": "user",
            "content": "Please write an essay about cats programmers.",
        }
    ],
    temperature=0.5,
    #top_p=1,
    model=model,
    stream=True
)

print(f'Response from {model}: \n')
for value in response:
  if value.choices:
    content = value.choices[0].delta.content
    if content:
      print(content, end='', flush=True)
#end='', it prevents new lines after each print
#flush=True, it forces the print to appear immediately