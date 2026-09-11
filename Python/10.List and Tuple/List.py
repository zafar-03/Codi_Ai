# collection Data data which is same or Different Data Type.
# Index : 0
# 1,1,2,3,4
# 12,"zafar",True

# Syntax : [1,1,2,3,4]

# mydata = [11,12,13]
# #          0  1  2

# print(mydata)
# print(type(mydata))

# How to Access Direct Value using Index :
# print(mydata[1])
# How to Modify Direct Value using Index :

# mydata[1] = 14
# print(mydata)


# Add : 
# mydata.append(100)
# print(mydata)


my_list = []

num = int(input("Enter the Number of Values : "))

for i in range(0,num):
    my_list.append(int(input("Enter Data : ")))

print(my_list)


# remove : 
my_list.pop()

print(my_list)

# reverse : 
my_list.reverse()
print(my_list)

# Sorting : 
# Asc
my_list.sort()
print(my_list)

# Desc
my_list.reverse()
print(my_list)