import json
import os

MEMORY_FILE = "data/conversation.json"


def load_memory():

    if not os.path.exists(
        MEMORY_FILE
    ):
        return []

    try:

        with open(
            MEMORY_FILE,
            "r"
        ) as f:

            return json.load(f)

    except:

        return []


def save_memory(history):

    with open(
        MEMORY_FILE,
        "w"
    ) as f:

        json.dump(
            history,
            f,
            indent=4
        )


def add_exchange(
    user_message,
    helios_reply
):

    history = load_memory()

    history.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": helios_reply
        }
    )

    save_memory(history)
