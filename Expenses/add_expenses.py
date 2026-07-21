import json
from pathlib import Path
from datetime import datetime

def get_id(expenses):
    
    if not expenses:
        return 1
    
    new_id = max(expense["ID"] for expense in expenses)
    return new_id + 1

def save_expenses(catogery, enter, total):

    file_path = (Path(__file__).resolve().parent.parent/"Data"/"Expenses.json")

    file_path.parent.mkdir(parents = True, exist_ok = True)

    if file_path.exists():
        try:
            with file_path.open("r", encoding = "utf-8") as f:
                expenses = json.load(f)

            if not isinstance(expenses, list):
                expenses = []

        except json.JSONDecodeError:
            expenses = []

    else:
        expenses = []

    new_id = get_id(expenses)

    

    date = datetime.now().strftime("%d-%m-%y")

    new_expense = {
        "ID": new_id,
        "Date": date,
        "Catogery": catogery,
        "Expenses": enter,
        "Total": total,

    }

    expenses.append(new_expense)

    with file_path.open("w", encoding = "utf-8") as f:
        json.dump(expenses, f ,indent = 2, ensure_ascii = False)

    return 'DONE\n'


def entry():

    catogery = input("\nEnter the catogery you spent on : ").strip()

    if not catogery:
        print("The catogery cannot be empty.")
        return None

    print("Enter your Expenses\n")

    enter = []

    exp = 0

    while True:

        amount = int(input("Enter Amount : "))
        spent = input("Spent on : ")
        enter.append((amount, spent))
        exp += amount

        while True:

            enters = input("\nEnter (YES) to continue the Entry if not enter (NO) : ")
            
            if enters.upper() == 'YES':
                break
            
            elif enters.upper() == 'NO':

                save_expenses(catogery, enter, exp)

                print("\nEntery completed !\n")
                return 'DONE'
            
            else:
                print("Invalid entry !")

        



if __name__ == "__main__":
    result = entry()

    