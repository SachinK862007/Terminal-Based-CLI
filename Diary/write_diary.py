import json
from pathlib import Path
from datetime import datetime


def get_next_id(diaries):

    if not diaries:
        return 1

    highest_id = max(diary["ID"] for diary in diaries)
    return highest_id + 1


def save_diary(lines, title):

    file_path = (Path(__file__).resolve().parent.parent/ "Data"/ "Data.json")

    # Create the Data folder if it does not exist.
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Load existing diary entries.
    if file_path.exists():
        try:
            with file_path.open("r", encoding="utf-8") as file:
                diaries = json.load(file)

            if not isinstance(diaries, list):
                diaries = []

        except json.JSONDecodeError:
            diaries = []

    else:
        diaries = []

    new_id = get_next_id(diaries)

    content = "\n".join(lines)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_diary = {
        "ID": new_id,
        "Date": current_time,
        "Title": title,
        "Content": content,
    }

    # Add the new dictionary to the existing diary list.
    diaries.append(new_diary)

    # Save the complete updated list.
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(diaries,file,indent=2,ensure_ascii=False,)

    return 'DONE\n'


def write():
    

    print('\nType "DONE" on a new line when you finish writing.')

    title = input("Enter title: ").strip()

    if not title:
        print("The title cannot be empty.")
        return None

    print("Enter your diary:")

    lines = []

    while True:
        new_line = input()

        if new_line.strip().upper() == "DONE":

            if not lines:
                print("The diary content cannot be empty.")
                continue

            while True:
                choice = input("\nEnter YES to save or NO to cancel: ").strip().lower()

                if choice == "yes":
                    saved_diary = save_diary(lines, title)

                    print(f'\nYour diary {title} has been added successfully.')

                    return 'Done\n'

                elif choice == "no":
                    print("\nThe diary has not been saved.")
                    return None

                else:
                    print("\nInvalid choice. Enter YES or NO.")

        else:
            lines.append(new_line)


if __name__ == "__main__":
    result = write()

    if result is not None:
        print("\nSaved diary:")
        print(result)