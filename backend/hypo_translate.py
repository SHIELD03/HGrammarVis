import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
model_id = 'gpt-3.5-turbo'
hypo_path = './hypoList.json'

# hypo_list = 'COUNT ( ) [ Origin = Europe ] < Count ( ) [! ( Origin = Europe ) ]'
with open(hypo_path, 'r') as file:
    hypo_list = json.load(file)

GPT_message = [
    {'role': 'system', 'content': ''},
    {'role': 'user', 'content': 'Translate these hypothesis to natural language, only reply with the translation results seperated with comma please: divide ( count() [ horsepower > 75 & horsepower < 125], count() ) > 0.75, corr ( acceleration, displacement) < -0.9, max ( horsepower ) [ model = pontiac ]  = max ( horsepower )'},
    {'role': 'assistant', 'content': 'Most values for Horsepower are in the range 75-125, Acceleration and Displacement have a strong inverse correlation, Pontiac Grand Prix has highest value for Horsepower'},
    {'role': 'user', 'content': 'Translate these hypothesis to natural language, only reply with the translation results seperated with comma please:' + ', '.join(hypo_list)}
]

GPT_response = response = openai.ChatCompletion.create(
  model=model_id,
  messages=GPT_message
)

print(GPT_response)
#print(GPT_response.choices[0].message.content)