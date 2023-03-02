# RunGPT
Interface to directly query OpenAI's GPT3 and (new) GPT3.5Chat API.

Note: you will first need to create a `_utils.py` file in the same directory, and assign a `apitoken` variable inside the `_utils.py`. Assign `apitoken` as your personal secret OpenAI API key.

### Usage:

(Optional tip): Setup an alias command in your .bash_profile to quickly startup the program using a shortcut.  


#### Text completion
From commandline:

To query davinci model (text completion): 
```bash
$ python gpt3.py
```

Then, directly type in your query to the input field:

```
What is the capital of Ottawa?
```

Exit python to quit the program.

#### ChatGPT API
From commandline:

To query chat model (gpt3.5-turbo): 
```bash
$ python chatgpt.py
```

First prompt (prime): prime the model as you wish, 
```
You are a travel agent.
```

Then, query the model in chat mode,

```
Give me a travel itinerary for a 5-day trip to New York City.
```

Exit python to quit the program.

