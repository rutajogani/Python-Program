student = {}
while True:
    print('1. Insert student recode')
    print('2. Update student recode')
    print('3. Delete student recode')
    print('4. Exit')

    choice = int(input('Enter the number that you want:'))

    if choice == 1:
        roll = int(input('Enter student Roll no:'))
        name = input('Enter student Name:')
        div = input('Enter student Division:')
        marks = input('Enter student Marks:')
        city = input('Enter student City:')

        student[roll]={
            "Name" == name,
            "Division" == div,
            "Marks" == marks,
            "City" == city
        }
        print('inserted successful')

    elif choice == 2:
        roll = int(input('Enter Roll no:'))
        if roll in student:
            student[roll]["Name"] = input('Enter new name:')
            student[roll]["Division"] = input('Enter new div:')
            student[roll]["Marks"] = input('Enter new marks:')
            student[roll]["City"] = input('Enter new city:')
        else: 
            print('student not found!')

        print('Updated successful')

    elif choice == 3:
        if roll == student:
            del student[roll] 
        else: 
            print('student not found!')
    
    elif choice == 4:
        print('Exiting program...')
        break
    
    else:
        print('invalid number')