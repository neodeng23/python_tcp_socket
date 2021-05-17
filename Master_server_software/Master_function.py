import sys
import json
import getpass

current_user = getpass.getuser()
file = "/Users/" + current_user + "/Desktop/master_config.json"


def read_json_config(file):
    with open(file) as json_file:
        config = json.load(json_file)
    return config