import json
from queue import Queue
import threading
from typing import Dict
from setup.config import data as config_data

_sentinel = object()

load_previous_data = config_data["load_previous_data"]
data_path = config_data['path']

def load_data():
    if load_previous_data:
        with open(data_path) as file:
            data = json.load(file)
        file.close()
        # inner fazer um inner_join
        # data = {**urls, **data}
        print("\nPrevious data loaded")
        return data
    else:
        print("\nPrevious data not loaded")
        # return urls


def write_data(data):
    with open(data_path, "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)
    file.close()

def write_append_data(append_data):
    with open(data_path, "r+") as file:
        data = json.load(file)
        data.update(append_data)
        file.seek(0)
        json.dump(data, file, indent=2, sort_keys=True)
    file.close()

## TERMINAR AQUI
def write_data_thread(data: Dict, write_queue: Queue):
    """Pretend we're saving a number in the database."""
    data = {}
    # while not hashing_event.is_set() or not write_queue.empty():
    while True:
        new_data = write_queue.get()
        if new_data is _sentinel:
            write_queue.put(_sentinel)
            break

        data.update(new_data)

        if len(data.keys()) > 10:
            print("\nAuxiliar: Writing Data to data.json\n")
            write_append_data(data)
            data.clear()
        
        #hash(urls)
        # -> hits_queue.put(hits)
        # -> write_queue.put(data)

        # logging.info(
        #     "Consumer storing message: %s (size=%d)", new_data, write_queue.qsize()
        # )

    # if data:
    print("\nAuxiliar: Writing remaining Data to data.json")
    write_append_data(data)
    print("Auxiliar: All data saved successfully\n")
    data.clear()


