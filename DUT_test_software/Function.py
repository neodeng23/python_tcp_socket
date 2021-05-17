import sys
import json
import getpass

current_user = getpass.getuser()
file = "/Users/" + current_user + "/Desktop/config.json"


def read_json_config(file):
    with open(file) as json_file:
        config = json.load(json_file)
    return config


if sys.platform == "darwin":
    from Quartz import (
        CGWindowListCopyWindowInfo,
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID
    )


def get_win_pos():
    win_name = []
    options = kCGWindowListOptionOnScreenOnly
    windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    for window in windowList:
        ownerName = window['kCGWindowOwnerName']
        geometry = window['kCGWindowBounds']
        win_name.append(ownerName)
        if ownerName == "Hyperion":
            return geometry["X"], geometry["Y"]
    if "Hyperion" not in win_name:
        return 9999, 9999


def get_test_result():
    pass
