# number1 = int(input("Enter the Value of number1 :"))
# # Nested If-else
# if(number1 > 0):
#     if(number1 % 5 == 0):
#         print("Number is Positive and Divisable by 5.")
#     else:
#         print("Number is Positive but not Divisable by 5.")
# else:
#     print("Number is Not Positive")

num1 = int(input("Enter the Value of N1 :"))
num2 = int(input("Enter the Value of N2 :"))
num3 = int(input("Enter the Value of N3 :"))



if(num1 > num2):
    if(num1 > num3):
        print("Number 1 is Greater")
    elif(num3 > num1) :
        print("Number 3 is Greater")
    else:
        print("Number 1 and Number 3 are same and Greater.")
elif(num2 > num1):
    if(num2 > num3):
        print("Number 2 is Greater")
    elif(num3 > num2) :
        print("Number 3 is Greater")
    else:
        print("Number 2 and Number 3 are same and Greater.")
else:
    if(num1 > num3):
        print("Number 1 and Number 2 are same and Greater.")
    elif(num3 > num1):
        print("Number 3 is Greater") 
    else:
        print("All are Equal")