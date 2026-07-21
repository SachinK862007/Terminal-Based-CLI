import json
from pathlib import Path

def reading():
    file_path = (Path(__file__).resolve().parent.parent/"Data"/"Expenses.json")

    with file_path.open("r", encoding = "utf-8") as f:
        data = json.load(f)

    print("\nExpexses Data")

    for i in data:
        print(f"ID = {i['ID']} : {i['Catogery']}")

    choise = int(input("\nEnter the 'ID' Number to see the Data : "))

    found = False

    for i in data:
        if choise == i["ID"]:
            found = True

            print(f"\nID : {i['ID']}")
            print(f"DATE : {i['Date']}")
            print(f"CATOGERY : {i['Catogery']}")
            
            for amount, spent in i['Expenses']:
                print(f"Amount = {amount}")
                print(f"Spent on = {spent}")
            print(f"\nTOTAL : {i['Total']}")
            break
    
    if not found:
        print("\nExpense Data not found !")

    while True:
        get_input = input("\nEnter Done if is complete : ")

        if get_input.upper() == 'DONE':
            return 'DONE\n'

if __name__ == '__main__':
    result = reading()