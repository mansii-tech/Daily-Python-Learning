# Program to manage student records
names = []  # empty list to store student tuples

while True:
    print("\n--- SELECT YOUR CHOICE ---")
    print("1 - Add student details")
    print("2 - Display all students")
    print("3 - Search student by roll number")
    print("4 - Delete student record")
    print("5 - Exit")

    choice = int(input("Enter choice: "))

    # 1. ADD STUDENT
    if choice == 1:
        r = int(input("Enter student roll number: "))
        n = input("Enter name: ")
        c = input("Enter course: ")
        stud = (r, n, c)
        names.append(stud)
        print("Student added successfully!")

    # 2. DISPLAY ALL
    elif choice == 2:
        if not names:
            print("No student records found.")
        else:
            print("\nList of Student Details:")
            for i in names:
                print(f"Roll No: {i[0]} | Name: {i[1]} | Course: {i[2]}")

    # 3. SEARCH STUDENT
    elif choice == 3:
        search_roll = int(input("Enter roll number to search: "))
        found = False
        for i in names:
            if i[0] == search_roll:
                print(f"Found! Roll No: {i[0]} | Name: {i[1]} | Course: {i[2]}")
                found = True
                break
        if not found:
            print("Student not found.")

    
    # 4. DELETE STUDENT
    elif choice == 4:
        delete_roll = int(input("Enter roll number to delete: "))
        found = False
        for i in names:
            if i[0] == delete_roll:
                names.remove(i)
                print("Student record deleted successfully!")
                found = True
                break
        if not found:
            print("Student not found.")

    # 6. EXIT
    elif choice == 5:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
