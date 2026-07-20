import json
from pathlib import Path

def lists():
    file_path = (Path(__file__).resolve().parent.parent/"Data"/"Data.json")

    with file_path.open("r", encoding = "utf-8") as f:
        item = json.load(f)

    print("\n===List of the Diaryes===")

    for i in item:
        print(f"{i['Title']}")

    while True:
        enter = input("\nType 'DONE' if it is done : ")

        if enter.upper() == 'DONE':
            return 'DONE\n'


if __name__ == '__main__':
    result = lists()


