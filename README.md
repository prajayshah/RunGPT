# RunGPT
Interface to directly query OpenAI's GPT3 API.

Note: you will need to assign a `apitoken` variable inside a `_utils.py` file before running this program. Assign `apitoken` as your personal secret OpenAI API key.

### Usage:

#### Text completion
From commandline:

To query davinci model (text completion): `$ python gpt3.py`

Then, directly type in your query to the input field that opens on the command line.

Exit python to quit the program.

#### ChatGPT API
From commandline:

To query chat model (gpt3.5-turbo): `$ python chatgpt.py`

First prompt (prime): prime the model as you wish, e.g. "you are a travel agent".

Then, query the model in chat mode, e.g. "Give me a travel itinerary for a 5-day trip to New York City".

Exit python to quit the program.

Optional tip: setup an alias command in your .bash_profile to quickly startup the program using a shortcut.  
