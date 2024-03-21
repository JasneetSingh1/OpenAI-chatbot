from openai import OpenAI

openai = OpenAI(
    api_key="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"
)

chatlog = []

while True:

    user_input = input()
    if user_input.lower() == 'stop':
        break

    chatlog.append({'role': 'user', 'content': user_input})

    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = chatlog,
        temperature= .6
    )
    bot_response = response.choices[0].message.content
    chatlog.append({'role': 'assistant', 'content': bot_response})
    print(bot_response)

