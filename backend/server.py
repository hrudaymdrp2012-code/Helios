from modules.routine import (
    add_task,
    get_tasks
)
from voice import speak
from flask_cors import CORS
from flask import (
    Flask,
    request,
    jsonify
)

from brain import ask_helios
from memory import (
    load_memory,
    add_exchange
)

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return "HELIOS ONLINE"


@app.route(
    "/chat",
    methods=["POST"]
)
def chat():

    data = request.json

    user_message = data["message"]

    history = load_memory()

    response = ask_helios(
        user_message,
        history
    )

    speak(response)

    add_exchange(
        user_message,
        response
    )

    return jsonify(
        {
            "response":
            response
        }
    )

@app.route(
"/routine/add",
methods=["POST"]
)
def routine_add():

    data = request.json

    add_task(

        data["task"],
        data["time"]

    )

    return jsonify({

        "status":"saved"

    })


@app.route(
"/routine/list"
)
def routine_list():

    return jsonify(

        get_tasks()

    )

if __name__ == "__main__":

    import os

app.run(
    host="0.0.0.0",
    port=int(
        os.environ.get(
            "PORT",
            8000
        )
    ),
    debug=False
)
