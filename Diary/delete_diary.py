import json
from pathlib import Path

def delete():

    file_path = (Path(__file__).resolve().parent.parent/"Data"/"Data.json")

    with file_path.open("r", encoding = "utf-8") as f:
        data = json.load(f)

    print ("\n List of the Diary entry\n")
    for i in data:
        print(f"ID = {i['ID']} : {i['Title']}")

    choise = int(input("\nEnter the ID of the Diary to delete : "))

    found = False

    for i in data:
        if choise == i["ID"]:
            while True:
                inputs = input("\nTo delete type (YES) if not to delete type (NO) : ")

                if inputs.upper() == 'YES':
                    break
                elif inputs.upper() == 'NO':
                    print("\nDiary not Deleted")
                    return
                else:
                    print("\nInvalid evtry !")

    for index, i in enumerate(data):
        if choise == i["ID"]:
            del data[index]

            with file_path.open("w", encoding = "utf-8") as f:
                json.dump(data, f, indent = 2)
            found = True
            print("Diary entry Deleted Successfully !")
            break
    
    if not found:
        print("\nDiary entry not Found\n")

    
   
if __name__ == '__main__':
    result = delete()
