import json
from pathlib import Path
from datetime import datetime

def summary():
    
    print("\n===Monthly Summary===\n")

    from datetime import datetime

    target_month = datetime.now().strftime("%m")
    date = datetime.now().strftime("%d-%m-%y")
    target_year = datetime.now().strftime("%y")
    month_name = datetime.strptime(date,"%d-%m-%y").strftime("%B")

    print(f"Month : {month_name}  {target_year}")

    file_path = (Path(__file__).resolve().parent.parent/"Data"/"Expenses.json")

    with file_path.open("r", encoding = "utf-8") as f:
        data = json.load(f)

    total_entries = len(data)
    print("Total Entries : ",total_entries)

    grand_total = 0

    for i in data:
        date = i["Date"]
        day, month, year = date.split("-")
        
        if (month == target_month) and (year == target_year):
            grand_total += i["Total"] 


    print("Grand Total : ",grand_total)

    
    while True:
        enter = input("\nEnter 'DONE' if completed : ")

        if enter.upper() == 'DONE':
            return 'DONE\n'


if __name__ == '__main__':
    result = summary()







