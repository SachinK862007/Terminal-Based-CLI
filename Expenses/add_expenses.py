import json
from pathlib import Path
from datetime import datetime

def get_id():
    
    if not expenses:
        return 1

    new_id = max(expenses["ID"] for expense in expenses)
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

    expense = "\n".join(enter)

    date = datetime.now().strftime("%d-%m-%y")

    new_expense = {
        "ID": new_id,
        "Date": date,
        "Catogery": catogery,
        "Expenses": expense,
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

    print("Enter your Expenses : ")

    enter = []

    exp = 0

    while True:

        amount = int(input("Enter Amount : "))
        spent = input("Spent on : ")

        exp += amount

        while True:

            enter = input("\nEnter (YES) to continue the Entry if not enter (NO)")

            if enter.upper() == 'YES':
                break
            
            elif enter.upper() == 'NO':

                save_entry = save_expenses(catogery, enter, total)

                print("\nEntery completed !\n")
                return 'DONE'
            
            else:
                print("Invalid entry !")

        if entry.upper() == 'YES':
            enter.append(amount, spent)



if __name__ == "__main__":
    result = entry()

    