from Diary.write_diary import write
from Diary.read_diary import read
from Diary.diary_list import lists
from Diary.delete_diary import delete
from Expenses.add_expenses import entry
from Expenses.view_expenses import view
from Expenses.delete_expenses import remove
from Expenses.entry_expenses import reading
from Expenses.summary import summary

print('=========================')
print(' Welcome to Your DIARY')
print('=========================')

while True:
    print('\n1.Diary')
    print('2.Expenses')
    print('3.Exit')
    choice = int(input('\nEnter your choice in number = '))

    if choice == 1:
        while True:
            print('\n1. Write a new Diary')
            print('2. Read the Diary')
            print('3. List all Diaries')
            print('4. Delete a Diary')
            print('5. Back to main menu')
            choice = int(input('\nEnter your choice in number = '))

            if choice == 1:
                result1 = write()
                print(result1)
            
            elif choice == 2:
                result2 = read()
                print(result2)

            elif choice == 3:
                result3 = lists()
                print(result3)

            elif choice == 4:
                result4 = delete()
                print(result4)

            elif choice == 5:
                break

            else:
                print('Invalid Choice')

            
    elif choice == 2:
        while True:
            print('\n1. Add expenses')
            print('2. View all expenses')
            print('3. Show monthly summary')
            print('4. Show the entry')
            print('5. Delete expense')
            print('6. Back to main menu')
            choice = int(input('\nEnter your choice in number = '))

            if choice == 1:
                result1 = entry()
                print(result1)

            elif choice == 2:
                result2 = view()
                print(result2)

            elif choice == 3:
                result3 = summary()
                print(result3)

            elif choice == 4:
                result4 = reading()
                print(result4)
            
            elif choice == 5:
                result5 = remove()
                print(result5)

            elif choice == 6:
                break

            else:
                print('Invalid Choice')

    elif choice == 3:
        break

    else:
        print('Invalid choice')

print('\n======================')
print(' Thankyou Come Again')  
print('======================')      

