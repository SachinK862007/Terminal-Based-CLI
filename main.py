from Diary.write_diary import write
from Diary.read_diary import read
from Diary.diary_list import lists
from Diary.delete_diary import delete

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
            print('4. Delete expense')
            print('5. Back to main menu')
            choice = int(input('\nEnter your choice in number = '))

            if choice == 1:
                pass

            elif choice == 2:
                pass

            elif choice == 3:
                pass

            elif choice == 4:
                pass
            
            elif choice == 5:
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

