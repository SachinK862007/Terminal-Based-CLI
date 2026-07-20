import json
from pathlib import Path

def read():

    file_path = (Path(__file__).resolve().parent.parent/"Data"/"Data.json")

    with file_path.open("r", encoding = "utf-8") as f:
        content = json.load(f)

        print("\nList of Diary Entry!")
        for i in content:
            print(f"{i["ID"]} : {i["Title"]}")
    
    choise = int(input("\nEnter the choise to read the diary : "))
    


    with file_path.open("r", encoding = "utf-8") as f:
        content = json.load(f)

    
    found = False
    
    for item in content:
        if choise == item["ID"]:

            found = True

            print(f"\nID : {item["ID"]}")
            print(f"DATE : {item["Date"]}")
            print(f"TITLE : {item["Title"]}")
            print("Content : ")
            print(f"{item["Content"]}\n")
            break
        
    if not found:
        print("\nDiary not Found !\n")
         
    while True:
        get_input = input("\nEnter Done if the reading is complete : ")

        if get_input.upper() == 'DONE':
            return 'DONE\n'
            


if __name__ == '__main__':
    read()