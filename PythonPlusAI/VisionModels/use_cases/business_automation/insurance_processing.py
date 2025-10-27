from openai import OpenAI
import os
import base64
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
endpoint = os.getenv("ENDPOINT")
model = os.getenv("MODEL")

def base64_encode_image(image_path):
    with open(image_path, "rb") as image_file:
        reading_file = image_file.read()
        image_encode = base64.b64encode(reading_file).decode("utf-8")
    return f"data:image/png;base64,{image_encode}" 

client = OpenAI(
  api_key=token, 
  base_url=endpoint
)

message =  [
    {
      "role": "system",
      "content": "You are an AI assistant that helps insurance companies process claims faster by extracting relevant information from images of documents."
    },
    {
      "role": "user",
      "content": [
        {
          "text": "Extract the policy number, claim amount, and date of incident from this insurance claim document.",
          "type": "text",
        },
        {
          "image_url": {
            "url": base64_encode_image("img/diagram_test.png")
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

print("response: ", response.choices[0].message.content)
