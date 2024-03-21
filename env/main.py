from openai import OpenAI


openai = OpenAI(
    api_key="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"
)

response = openai.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{
        'role': 'system',
        'content': 'You are a helpful assistant'
    }, {}]
)

print(response.choices[0].message.content)