import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"

client = OpenAI(api_key=API_KEY)

prompt = "Hello there!"

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "system", "content": prompt}]
)

print(response.choices[0].message.content)