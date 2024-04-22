import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Sos un asistente virtual que esta para ayudar"},
    {"role": "user", "content": "Cuantos albumes saco Michael Jackson"}
  ]
)

print(completion.choices[0].message.content)

prompt_tk = completion.usage.prompt_tokens
completion_tk = completion.usage.completion_tokens

print("Completion Tokens= ", completion_tk)
print("Completion Tokens= ", prompt_tk)

#	Input $0.0015 / 1K tokens	Output $0.002 / 1K tokens

Costo_input = prompt_tk * 0.0015 / 1000
Costo_output = completion_tk * 0.002 / 1000

print("Costo final = ", Costo_input + Costo_output)