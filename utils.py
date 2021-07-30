import json


def load_data():
    with open("data.json") as file:
        data = json.load(file)
    file.close()
    return data


def write_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)
    file.close()

