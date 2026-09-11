# Q.1 Find and print the index of the maximum and minimum values.
# my_list1 = [34,67,89,34,23,11,3,4]

# print(my_list1)
# print("Maximum Value :",max(my_list1))
# print("Minimum Value :",min(my_list1))

# print("index of Maximum Value :",my_list1.index(max(my_list1)))
# print("index of Minimum Value :",my_list1.index(min(my_list1)))

# ========================================================================
# Q.2 Compute and print the cumulative sum of the array.

# my_Arr = [
#     [1,4,7],
#     [2,5,8],
#     [3,6,9]
# ]

# my_Arr_copy = my_Arr.copy()


# for i in range(0,len(my_Arr)):
#     for j in range(0,len(my_Arr[i])):
#         if i==0:
#             my_Arr_copy[i][j] = my_Arr[i][j] + 0
#         else:
#             my_Arr_copy[i][j] = my_Arr[i][j] + my_Arr_copy[i-1][j]


# for element in my_Arr_copy:
#     print(element)
# print(my_Arr_copy)

# =========================================================================
# Q.3 Find the unique elements and their frequency count in an array.
# my_list1 = [34,67,89,34,3,3,23,11,67,3,4]

# my_set = set(my_list1)

# # print(my_list1,my_set)
# for element in my_set:
#     print(element,"->",my_list1.count(element))

# Q.4 Extract all numbers that are divisible by 3 from the array.
# my_list1 = [33,67,89,33,3,3,23,15,67,3,4]
# print(my_list1)

# for element in my_list1:
#     if element % 3 == 0 :
#         print(element)


# Q.5 Generate the first N Fibonacci numbers and create an array of that. Where, N=User Input.

# 0 , 1 , 1 , 2 , 3 , 5, 8
# a   b
#        c

#     a  b

# a = 0
# b = 1
# num = int(input("Enter the Value of N : "))

# for i in range(0,num+1):
#     print(a,end=",")
#     c = a + b
#     a = b 
#     b = c
