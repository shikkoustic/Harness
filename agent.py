import os
from openai import OpenAI
import json
import tools

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
    max_retries=1,
)

messages=[
  {"role": "system", "content": "Hello, I'm an Assistant"},
]

while True:
  user_input = input("You: ")
  if(user_input.lower() == "exit"):
    break

  messages.append({"role": "user", "content": user_input})

  while True:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools = tools.get_schemas(),
    )

    reply = response.choices[0].message

    if reply.tool_calls:
      messages.append(reply)

      for tool_call in reply.tool_calls:
        name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        result = tools.call_tool(name, arguments)

        messages.append({
          "role": "tool",
          "tool_call_id": tool_call.id,
          "content": result,
        })
        continue

    print("Assistent: ", reply.content)
    messages.append({"role": "assistant", "content": reply.content})
    break

