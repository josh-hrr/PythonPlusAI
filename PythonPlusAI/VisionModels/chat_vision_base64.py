

'''

rb = read binary
''' 
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

def base64_encode_image(image_path):
    with open(image_path, "rb") as image_file:
        reading_file = image_file.read()
        image_encode = base64.b64encode(reading_file).decode("utf-8")
    return f"data:image/png;base64,{image_encode}" 



load_dotenv()
token = os.getenv("GITHUB_TOKEN")
endpoint = os.getenv("ENDPOINT")
model = os.getenv("MODEL")

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": [
                {"text": "are these alligators or crocodiles?", "type": "text"},
                {"image_url": {"url": base64_encode_image("img/mystery_reptile.png")}, "type": "image_url"},
            ],
        }
    ],
)

print(response.choices[0].message.content)