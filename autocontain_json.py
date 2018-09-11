import argparse
import json


class JSONObject(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


def json_to_docker(json):
    # Accepts JSON object and writes temporary Dockerfile
    # Outputs Dockerfile path

    for d in json:
        print(d)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Function for converting from JSON to Dockerfile")

    parser.add_argument("-j", "--json", help="JSON file input")
    args = parser.parse_args()

    with open(args.json, 'r') as f:
        json_data = json.load(f)

    try:
        json_to_docker(json_data)
    except:
        print("Unable to read JSON data")
