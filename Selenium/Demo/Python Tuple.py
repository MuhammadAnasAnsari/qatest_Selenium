#Tuple are similar with teh list but we can change the values of the tuples

my_tuple=("Apple", "grapes", "Orange")
# To find the length of tuple
print(len(my_tuple))

print(my_tuple)
print(my_tuple[0]) # To print the specific value of the tuple

print(my_tuple[-1]) #Negative values starts from the last of the tuple

print(my_tuple[0:2]) # To print the multiple indexed values

 #to print all the values in the tuple with For Loop
for val in my_tuple:
    print(val)

# Tuple values are unchangeable test
# my_tuple[1]="Cherry"     # TypeError: 'tuple' object does not support item assignment

# Tuple values are not deleteable test
# del my_tuple[1]        # TypeError: 'tuple' object doesn't support item deletion

#To delete the entire tuple i.e valid
# del my_tuple
# print(my_tuple)  # NameError: name 'my_tuple' is not defined [test: Passed]

# Nested Tuple with different data types and inside list
my_tuple_2=("Punjab", (1, 3, 5) , -23.40, 4.90, 23, ["Apple", 2])
print(my_tuple_2) # To print the entire tuple

# print(my_tuple_2[2][1])  # TypeError: 'float' object is not subscriptable

print(my_tuple_2[1][2])  # to print the nested tuple index within the index

# my_tuple_2[2]=12346   # TypeError: 'tuple' object does not support item assignment

my_tuple_2[5][1]="Pindi" # To print change/assign new value to the list in the tuple [valid]
print(my_tuple_2)

#To check the values present or not in the tuple
print("Banana" in my_tuple) #False
print(-23.40 in my_tuple_2) #True