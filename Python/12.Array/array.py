# list : 
# collection of values which is same or different datatype.
# array (matrix)

"""
- There are two types.
1. 1-D Array 



2. 2-D Array (Multi-D)
"""
"""
Q.1 Create a 1D array (list) with five integer elements. Display the array using a loop.

Q.2 Develop a program to calculate the sum of all elements in a 1D array separately.


Q.4 Create a program to insert a new element at a specific position(index) in a 1D array.
"""
# my_arr = [11,23,45,67,89]
# #          0  1  2  3  4

# for element in my_arr:
#     print(element,end=" ")

# # print("\nSum is : ",sum(my_arr))

# index = int(input("\nEnter position(index) No. : "))
# del my_arr[index]
# # my_arr[index] = int(input("Enter the New Value"))
# for element in my_arr:
     if element % 2 ==0:
#     print(element,end=" ")


# my_arr = [11,45,67,89,23]
# value = int(input("Enter the Value :"))
# print(my_arr.index(value))


# my_arr1 = [11,23]
# my_arr2= [45,67,89]


# print(my_arr1 + my_arr2)
# my_arr1.extend(my_arr2)
# print(my_arr1)

# print(my_arr)
# my_arr.sort()
# print(my_arr)

# print(sorted(my_arr))
# print(my_arr)


# =============================
# my_arr = [1,2,3,4,5]

# length = 0
# add = 0
# for element in my_arr:
#     add += element
#     length+=1

# print(add / length)


"""
a1 = [1,2,3,4]
a2 = [5,6,7,8]

sum =[6,8,10,12] 
"""

my_arr1 = [1,2,3,4]
my_arr2 = [5,6,7,8]

sum_arr = []

for i in range(0,len(my_arr1)):
    sum_arr.append(my_arr1[i] + my_arr2[i])

print(sum_arr)