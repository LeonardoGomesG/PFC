import json

from setup.config import data as config_data


def load_data(urls):
    if config_data["load_previous_data"]:
        with open("data.json") as file:
            data = json.load(file)
        file.close()
        # inner fazer um inner_join
        data = {**urls, **data}
        print("\nPrevious data loaded")
        return data
    else:
        print("\nPrevious data not loaded")
        return urls


def write_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)
    file.close()

