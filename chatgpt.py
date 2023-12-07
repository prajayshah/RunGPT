import sys

import openai
from _utils import apikey
import pyttsx3
from pynput import keyboard


"""
usage:

To start chatbot:
$ chatgpt

To start chatbot in speech reply mode, the chatbot will speak the response of each output:
$ chatgpt speech
"""


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


def speak_response(input_to_speak: str):
    print(input_to_speak)
    engine = pyttsx3.init()
    engine.say(input_to_speak)
    engine.runAndWait()


def speak_response_opt_interrupt(input_to_speak: str):
    "not stable yet - this only stops the speech on one iteration, does not interrupt speech on multiple iterations."
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # # Create a flag to control the speech output
    # stop_speech = False

    # Define a function to handle keypress events
    def on_key_release(key):
        global stop_speech
        if key == keyboard.Key.shift_l:
            print('Key was pressed')
            stop_speech = True
            return False

    # Register the keypress event listener
    listener = keyboard.Listener(on_release=on_key_release)
    listener.start()



    # Start the text-to-speech output
    def onWord(name, location, length):
        # print ('word', name, location, length)
        if stop_speech:
            print('stopping output')
            engine.stop()
            # listener.stop()
            # stop_speech = False

    print(input_to_speak)

    engine.connect('started-word', onWord)
    engine.say(input_to_speak)
    engine.runAndWait()


def ChatGPT_Completion(to_speech: bool = False):
    response = openai.ChatCompletion.create(
        model=ENGINE,
        messages=MESSAGES
    )
    _append_new_message(_new_assistant_message(response.choices[0].message.content))
    if not to_speech:
        # just print out the response:
        return print(response.choices[0].message.content)
    else:
        # print out the response and also provide speech output of the response
        return speak_response(input_to_speak=response.choices[0].message.content)
        # return speak_response_opt_interrupt(input_to_speak=response.choices[0].message.content)


if __name__ == '__main__':
    sys.argv.append('speech')
    to_speech = True if (len(sys.argv) > 1 and 'speech' in sys.argv[1]) else False
    flag = True
    system_prime = str(input(f'Prime {ENGINE}: '))
    if system_prime and ('prime' in system_prime[:5] or 'Prime' in system_prime[:5]): system_message = {'role': 'system', 'content': system_prime[6:]}
    else: system_message = {"role": "system", "content": "You are a helpful assistant."}

    _append_new_message(system_message)

    while flag:
        print('\n')
        try:
            query = str(input(f'Query {ENGINE}: '))
            _append_new_message(_new_user_message(query))
            ChatGPT_Completion(to_speech)
            print('\n')
        except EOFError or KeyboardInterrupt:
            print('exiting..')
            break

