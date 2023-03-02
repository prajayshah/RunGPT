import openai
from _utils import apikey

## Call the API key under your account (in a secure way)
openai.api_key = apikey
ENGINE = "gpt-3.5-turbo"
MESSAGES = []

def _append_new_message(message):
    MESSAGES.append(message)

def _new_user_message(texts):
    return {'role': 'user', 'content': texts}

def _new_assistant_message(texts):
    return {'role': 'assistant', 'content': texts}

def ChatGPT_Completion():
    response = openai.ChatCompletion.create(
        model=ENGINE,
        messages=MESSAGES
    )
    _append_new_message(_new_assistant_message(response.choices[0].message.content))
    return print(response.choices[0].message.content)


if __name__ == '__main__':
    a = True
    system_prime = str(input(f'Prime {ENGINE}: '))
    if system_prime and ('prime' in system_prime[:5] or 'Prime' in system_prime[:5]): system_message = {'role': 'system', 'content': system_prime[6:]}
    else: system_message = {"role": "system", "content": "You are a helpful assistant."}

    _append_new_message(system_message)

    while a:
        print('\n')
        try:
            query = str(input(f'Query {ENGINE}: '))
        except EOFError:
            break

        _append_new_message(_new_user_message(query))
        ChatGPT_Completion()
        print('\n')
