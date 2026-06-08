from memory import (
    load_memory,
    add_exchange
)
from groq import Groq

import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are HELIOS.

A futuristic AI assistant.

Traits:
- intelligent
- calm
- concise
- loyal to HC
- futuristic

Never mention ChatGPT.

Address the user as HC when appropriate.
"""

def ask_helios(user_input, history=None):

    if history is None:
        history = []

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7
    )

    return completion.choices[0].message.content


if __name__ == "__main__":

    while True:

        user = input("HC > ")

        if user.lower() in [
            "exit",
            "quit"
        ]:
            break

        history = load_memory()

        response = ask_helios(
            user,
            history
        )

        add_exchange(
            user,
            response
        )

        print(
            "\nHELIOS >",
            response,
            "\n"
        )
