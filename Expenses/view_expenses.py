import json
from pathlib import Path

def view():
    file_path = (Path(__file__).resolve().parent.parent/"Data"/"Expenses.json")

    with file_path.open("r", encoding = "utf-8") as f:
        item = json.load(f)

    print("\n===List of Expenses===")

    for i in item:
        print(f"{i['Date']}")
        print(f"{i['Catogery']} = {i['Total']}\n")
        
    while True:
        enter = input("\nType 'DONE' if completed : ")

        if enter.upper() == 'DONE':
            return 'DONE\n'

if __name__ == '__main__':
    result = view()