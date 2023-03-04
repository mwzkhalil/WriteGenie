import requests
import json
from WriteGenie import app

def suggest_alternatives(text):
    api_key = app.config['API_KEY']
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {api_key}"}
    data = {
        "prompt": f"What are some alternative words for {text}?",
        "max_tokens": 50,
        "temperature": 0.7,
        "n": 1,
        "stop": "\n"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        return "Unable to suggest alternatives at this time."
