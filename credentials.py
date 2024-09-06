import os
from dotenv import load_dotenv, find_dotenv

#Load the .env file
load_dotenv(find_dotenv)

openai_api_key = os.getenv("OPENAI_API_KEY")