# CRUD with List  []: 

# CRUD :
# C : create  : new data add
# R : read    : data print 
# U : update  : data modify 
# D : delete  : data remove



my_list = []
#          0   1  2
# len    : 3


while True:
    print("\n","="*10,"CRUD Operation","="*10)
    print("1. for Add New Data")
    print("2. for Display All Data")
    print("3. for Update Data")
    print("4. for Delete Data")
    print("5. for Exit")

    choice = int(input("Enter Your Choice : "))

    if choice==1:
        my_list.append(input("Enter new Data :"))
        print("Data Successfully Added!!\n")

    elif choice==2:
        print("All Data :",end="")
        for data in my_list:
            print(data,end=",")
        print()

    elif choice==3:
        my_index = int(input("Enter Index Number : "))
        if my_index < len(my_list):
            my_list[my_index] = input("Enter new Data :")
            print("Data Changed Successfully!!\n")
        else:
            print("Data Doesn't Exist!!\n")
        
    elif choice==4:
        newdata = input("Enter Value which do you want to remove : ")

        if newdata in my_list:
            my_list.remove(newdata)
            print("Data Removed Successfully!!")
        else:
            print("Data Doesn't Exist!!\n")

    elif choice==5:
        break
    else:
        print("Please Enter Valid Choice!!")


print("Program Terminate")