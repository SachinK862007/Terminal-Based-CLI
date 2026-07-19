from Diary.write_diary import write

print('=========================')
print(' Welcome to Your DIARY')
print('=========================')

while True:
    print('1.Diary')
    print('2.Expenses')
    print('3.Exit')
    choice = int(input('Enter your choice in number = '))

    if choice == 1:
        while True:
            print('1. Write a new Diary')
            print('2. Read the Diary')
            print('3. List all Diaries')
            print('4. Delete a Diary')
            print('5. Back to main menu')
            choice = int(input('Enter your choice in number = '))

            if choice == 1:
                result = write()
                print(result)
            
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

            
    elif choice == 2:
        while True:
            print('1. Add expense')
            print('2. View all expenses')
            print('3. Show monthly summary')
            print('4. Delete expense')
            print('5. Back to main menu')
            choice = int(input('Enter your choice in number = '))

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

print('======================')
print(' Thankyou Come Again')  
print('======================')      

