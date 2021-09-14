import time
import hashlib
import requests


def compare_hashes(data):
    print("\nCalculating Hashes")
    time.sleep(1)
    diff = 0
    for url_path in data.keys():
        try:
            response = requests.get(url_path).text.encode('utf-8')
            # create a hash
            new_hash = hashlib.md5(response).hexdigest()

            # check if new hash is same as the previous hash
            if new_hash == data[url_path]:
                continue

            # if something changed in the hashes
            else:
                # notify
                print("Hash difference for: ", url_path, ": ", data[url_path])
                print("new_hash: ", new_hash, "\n")
                data[url_path] = new_hash
                diff += 1
                continue

        # To handle exceptions
        except Exception as e:
            print("error")

    print(diff, "differences found")
    return data
