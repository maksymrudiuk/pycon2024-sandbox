import os
from openai import OpenAI
import instructor
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Initialize with API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Enable instructor patches for OpenAI client
client = instructor.from_openai(client)

class User(BaseModel):
    name: str
    age: int

# Create structured output
user = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Extract: Maksym is 25 years old"},
    ],
    response_model=User,
)

print(user)