import json
from pathlib import Path

def remove():

    file_path = (Path(__file__).resolve().parent.parent/"Data"/"Expenses.json")

    with file_path.open("r", encoding = "utf-8") as f:
        item = json.load(f)

    print("\nList of Expenses\n")
    for i in item:
        print(f"ID = {i['ID']} : {i['Catogery']} Amount = {i['Total']}")

    choise = int(input("\nEnter the 'ID' number to Delete the expenses : "))

    found = False

    for index, i in enumerate(item):
        if choise == i['ID']:
            
            found = True

            while True:
                enter = input("\nTo Delete type (YES) if not to Delete type (NO) : ")

                if enter.upper() == 'YES':
                    del item[index]

                    with file_path.open("w", encoding = "utf-8") as f:
                        json.dump(item, f, indent = 2)
                    
                    

                    print("\nExpense entry deleted !\n")
                    break
                
                elif enter.upper() == 'NO':
                    print("\nExpense entry not deleted\n")
                    break

                else:
                    print("\nInvalid Input")

    if not found:
        print("\nExpense Entry Not Found !\n")

    while True:
        enter = input("Enter 'DONE to go back to menu : ")

        if enter.upper() == 'DONE':
            return 'DONE\n'

if __name__ == '__main__':
    result = remove()