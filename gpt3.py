import openai
from _utils import apikey

## Call the API key under your account (in a secure way)
openai.api_key = apikey


def GPT_Completion(texts):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=texts,
        temperature=0.6,
        top_p=1,
        max_tokens=500,
        frequency_penalty=0,
        presence_penalty=0
    )
    return print(response.choices[0].text)


if __name__ == '__main__':
    a = True
    while a:
        print('\n')
        query = str(input('Query GPT-3: '))
        GPT_Completion(query)
        print('\n')
