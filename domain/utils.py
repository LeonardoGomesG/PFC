import json

def load_data(urls, load_previous_data, path):
    if load_previous_data:
        with open(path) as file:
            data = json.load(file)
        file.close()
        # inner fazer um inner_join
        data = {**urls, **data}
        print("\nPrevious data loaded")
        return data
    else:
        print("\nPrevious data not loaded")
        return urls


def write_data(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)
    file.close()

