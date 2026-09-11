all_students = []

print("Welcome to Student Data Oeganizer!")

while True:
    print("\nSelect an Option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subject Offered")
    print("6. Exit")
    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        print("\nEnter student Details:")
        all_students.append({
                    "roll_no" : (input("Enter ID:"),),
                    "student_name" : input("Name:"),
                    "student_age" : int(input("Age:")),
                    "student_grade" : input("Grade:"),
                    "student_dob" : (input("Date of Birth (YYYY-MM-DD):"),),
                    "student_subjects" :  set(input("Subjects (comma-seprated):").split(","))
                })
        print("\nstudent added Successfully!")

        
    elif choice == 2:
        for data in all_students:
            print(data)

    elif choice == 3:
        user_data = input("Enter Roll_no")
        my_list2 = []
        for data in all_students:
            if (user_data,) == data.get("roll_no"):
                my_list2.append({
                    "roll_no" : data.get("roll_no"),
                    "student_name" :  data.get("student_name"),
                    "student_age" : int(input("Age:")),
                    "student_grade" : input("Grade:"),
                    "student_dob" : data.get("student_dob"),
                    "student_subjects" :  set(input("Subjects (comma-seprated):").split(","))
                })
            else:
                my_list2.append(data)
        all_students = my_list2
        print("Updated Successfully")

    elif choice == 4:
        user_data = input("Enter Roll_no")
        my_list2 = []
        for data in all_students:
            if (user_data,) == data.get("roll_no"):
                pass
            else:
                my_list2.append(data)
        all_students = my_list2
        print("Deleted Successfully")
        
    elif choice == 5:
        user_data = input("Enter SubjectName :")
        for data in all_students:
            if user_data in data.get("student_subjects"):
                print(data)
        
    elif choice == 6:
        print("Program Terminate")
        break
    else:
        print("Please Enter Valid Choice!!")

