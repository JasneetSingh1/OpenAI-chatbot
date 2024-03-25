from openai import OpenAI
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


openai = OpenAI(
    api_key="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"
)

chatlog = [{'role': 'system',
            'content': 'You are a Python tutor AI, completely dedicated to teach users how to learn Python \
                       from scratch. Please provide clear instructions on Python concepts, best practices, \
                       and syntax. Help create a path of learnting for users to be able to create real life, \
                       production ready python applications.'}]

chat_responses = []

@app.post("/", response_class=HTMLResponse)
async def chat(request:Request, user_input: Annotated[str, Form()]):


    chatlog.append({'role': 'user', 'content': user_input})
    chat_responses.append(user_input)

    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = chatlog,
        temperature= 0.6
    )
    bot_response = response.choices[0].message.content
    chatlog.append({'role': 'assistant', 'content': bot_response})
    chat_responses.append(bot_response)
    return templates.TemplateResponse("home.html", {"request":request, "chat_responses": chat_responses})

