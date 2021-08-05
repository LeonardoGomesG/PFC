import json

import config


def load_data():
    if config.data["load_previous_data"]:
        with open("data.json") as file:
            data = json.load(file)
        file.close()
        print("\nPrevious data loaded")
        return data
    else:
        print("\nPrevious data not loaded")
        return {}


def write_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)
    file.close()

