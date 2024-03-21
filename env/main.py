from openai import OpenAI
from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

openai = OpenAI(
    api_key="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"
)

chatlog = []

@app.post("/")
async def chat(user_input: Annotated(str, Form())):


    chatlog.append({'role': 'user', 'content': user_input})

    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = chatlog,
        temperature= 0.6
    )
    bot_response = response.choices[0].message.content
    chatlog.append({'role': 'assistant', 'content': bot_response})
    return bot_response

