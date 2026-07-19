import json
from pathlib import Path
from datetime import datetime

def appending(lin, tit):
    new_diary = {}

    date = datetime.now()
    line = '\n'.join(lin)
    title = tit

    file_path = Path('..\python\Terminal-Based-CLI\Data\Data.json')

    with file_path.open("r", encoding="utf-8") as f:
        diaries = json.load(f)
        new_id = len(diaries)+1 
        

    new_diary["ID"] = new_id
    new_diary["Date"] = date
    new_diary["Title"] = title
    new_diary["Content"] = line

    with file_path.open('w', encoding = "utf-8") as f :
        json.dump(new_diary, f, indent=2)



    


def write():

    while True:
        print('Please enter "DONE" in the new line after the complition of the Diary writing')
        title = input("Enter Title : ")
        print("Enter your Diary")

        line = []
        
        while True:
            
            new_line = input (" ")
        
            if new_line == 'DONE':

                while True:
                    choise = input("Enter (YES) if confirmed or (NO) not to save : ")

                    if (choise == 'YES') or (choise == 'yes'):
                        
                        appending(line, title)
                        print(f"Your diary {title} have been Added Successfully")
                        return 'DONE'

                    elif (choise == 'NO') or (choise == 'no'):
                        print('The Diary have not been saved !')
                        return None

                    else:
                        print('Invalid Choise. Please enter the valid choice')

            line.append(new_line)
                

                      

        


w = write()

print(w)