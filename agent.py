import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ["GROQ_API_KEY"],
  base_url="https://api.groq.com/openai/v1",
)

messages=[
  {"role": "system", "content": "Hello, I'm an Assistant"},
  {"role": "user", "content": "What is Agent Harness?"},
]

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
)
print(response.choices[0].message.content)
