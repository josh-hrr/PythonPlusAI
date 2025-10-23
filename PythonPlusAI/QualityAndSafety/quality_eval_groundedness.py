import os

import azure.identity
import rich
from azure.ai.evaluation import (
    AzureOpenAIModelConfiguration,
    GroundednessEvaluator,
    OpenAIModelConfiguration,
)
from dotenv import load_dotenv

# Setup the OpenAI client to use either Azure or GitHub Models
load_dotenv(override=True)
API_HOST = os.getenv("API_HOST", "github")

token = os.getenv("GITHUB_TOKEN")
endpoint = os.getenv("ENDPOINT")
model = os.getenv("MODEL")

if API_HOST == "azure":
    credential = azure.identity.DefaultAzureCredential()
    token_provider = azure.identity.get_bearer_token_provider(
        credential, "https://cognitiveservices.azure.com/.default"
    )
    model_config: AzureOpenAIModelConfiguration = {
        "azure_endpoint": os.environ["AZURE_AI_ENDPOINT"],
        "azure_deployment": os.environ["AZURE_AI_CHAT_DEPLOYMENT"],
    }
elif API_HOST == "github":
    model_config: OpenAIModelConfiguration = {
        "type": "openai",
        "api_key": token,
        "base_url": endpoint,
        "model": model,
    }

query = "Given the product specification for the Contoso Home Furnishings Dining Chair, provide an engaging marketing product description."
context = 'test'
response = 'Introducing our timeless wooden dining chair, designed for both comfort and durability. Crafted with a solid teak seat and sturdy four-legged base, this chair offers reliable support for up to 250 lbs. The smooth brown finish adds a touch of rustic elegance, while the ergonomically shaped backrest ensures a comfortable dining experience. Measuring 18" wide, 20" deep, and 35" tall, it\'s the perfect blend of form and function, making it a versatile addition to any dining space. Elevate your home with this beautifully simple yet sophisticated seating option.'

groundedness_eval = GroundednessEvaluator(model_config)
groundedness_score = groundedness_eval(
    query=query,
    context=context,
    response=response,
)
rich.print(groundedness_score)
