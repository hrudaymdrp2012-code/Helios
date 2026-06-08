import json

FILE = "data/routines.json"

def load_routines():

    try:

        with open(FILE,"r") as f:
            return json.load(f)

    except:

        return []

def add_task(task,time):

    routines = load_routines()

    routines.append({

        "task":task,
        "time":time

    })

    with open(FILE,"w") as f:

        json.dump(
            routines,
            f,
            indent=4
        )

def get_tasks():

    return load_routines()
