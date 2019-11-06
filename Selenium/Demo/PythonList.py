my_list = ["Tokyo", "London", "New York", "", ""]
# To print the list
print(my_list)

# To the list values by index
# print(my_list[1],my_list[2],my_list[0])
print(my_list[0])

# To insert/assign the new value of the index already present in the list
my_list[3] = "India"
my_list[4] = "Japan"
print(my_list)

# To print all the values in the list with For loop
for val in my_list:
    print(val)

#To append new new value in the list
my_list.append("America")
# my_list.append("Pakistan", "South Africa", "America", "Nigeria")  #We should only append a single value
# #--->>     my_list.append("Pakistan", "South Africa", "America", "Nigeria")
# ['Tokyo', 'London', 'New York', 'India', 'Japan']
# TypeError: append() takes exactly one argument (4 given)

print(my_list)

#To Insert the values in the list with index position defined (pulling back other indexes)
my_list.insert(0,"Pakistan")

print(my_list)

#To remove the element / object from the list
my_list.remove("Tokyo")

print(my_list)

#To pop the value from the list
my_list.pop() # (remove the last value)
print(my_list)

my_list.pop(3) # (remove the 3rd index value)
print(my_list)

# To Clear the list
my_list.clear()
print(my_list)

#To reverse the list values
fruits=["Apple", "Cherry", "Peach", "Mango", "Banana", "Orange"]
print(fruits)

fruits.reverse()
print(fruits)

# Create list with different data types
my_list_2=[12.5, 0, -98.60, "Arham", [1,9,89]]
my_list_3=["Apple iPhoneX", [1,2,3], [10,20,89.90,-90.01]]

# To find the length of the list
print(len(my_list))
print(len(my_list_2))
print(len(my_list_3))

#To acces the list index and inside the index next index
print(my_list_3[4][1])

