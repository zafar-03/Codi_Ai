# print("Hello")
# print("Hello")
# print("Hello")

# #100

# Loop : 
# 1. for Loop

# for i in range(50,100):
#     print(i,"Hello")

# WAP to Print 1 to n Numbers.
# num = int(input("Enter the Value of N : "))

# for j in range(1,num+1):
#     print(j)



# WAP to print no. n Table.
"""
2*1 = 2
..

2*10 = 20
"""
# n = int(input("Enter the Value of N : "))

# for t in range(1,11):
#     print(n,"*",t,"=",n*t)


# List : []

# mylist = [23,67,967,34,22]
# for element in mylist:
#     print(element)



# WAP to Print Square given Numbers.
# mydata = [34,1,23,56,70,10]

# for i in mydata:
#     print(i*i)



##########################################
# WAP to print Factorial of Given Number : 
"""
4
4 * 6 = 24

0
"""
# n = int(input("Enter the Value of N : "))
# fact = 1

# for i in range(1,n+1):
#     fact = fact*i

# print("Factorial : ",fact)


# WAP to Print Sum of All Even Number by given range

# num1 = int(input("Enter N1 :"))
# num2 = int(input("Enter N2 :"))
# sumAll = 0

# if(num1>num2):
#     temp = num1
#     num1 = num2
# #     num2 = temp

# for i in range(num1,num2):
#     if( i % 2 == 0):
#         sumAll = sumAll+i

# print(sumAll)# 2,4,6,8,10



"""
1. Write a C program to display the n terms of odd natural numbers and their sum.

Test Data
Input number of terms : 10
Expected Output :
The odd numbers are :1 3 5 7 9 11 13 15 17 19
The Sum of odd Natural Number upto 10 terms : 100


2. Write a C program to display the sum of n terms of even natural numbers.

Test Data :
Input number of terms : 5
Expected Output :
The even numbers are :2 4 6 8 10
The Sum of even Natural Number upto 5 terms : 30
"""

# num = int(input("Input number of terms :"))
# sum = 0
# print("The odd numbers are :",end="")
# for i in  range(1,(num*2)+1):
#     if(i%2!=0):
#         # sum+=i 
#         sum = sum + i
#         print(i,end=" ")

# print("")
# print("The Sum of odd Natural Number upto 10 terms :",sum)




# num = int(input("Input number of terms :"))
# sum = 0
# print("The even numbers are :",end="")
# for i in  range(1,(num*2)+1):
#     if(i%2==0):
#         # sum+=i 
#         sum = sum + i
#         print(i,end=" ")

# print("")
# print("The Sum of even Natural Number upto",num,"terms :",sum)