my_set={1, 3, "chalk", 90, "Apple"}
print(my_set)

# In sets we are unable to access the values with index
# print(my_set[1]) # TypeError: 'set' object is not subscriptable

#To print all the value sin the set with for loop
for x in my_set:
    print(x)

# To check the valies present or not in the set
print("Apple" in my_set) # True
print(-23.50 in my_set)  # False

# To Add any value in the set
# my_set.add("Punjab", -23.348)  # TypeError: add() takes exactly one argument (2 given)
my_set.add(-23.834) # Add value anywhere in the list
print(my_set)


# To Add multiple values in the set with update()
my_set.update(["Pakistan", 25, 0.98, -45.90, "Success...!"])
print(my_set)

# To find the length of the set
len(my_set)

#To discard the set
my_set.discard("Lollipop") # Use when we are not sure value present in the set
print(my_set)

# To remove value in the set
my_set.remove("Apple") # Use when We are sure the value is present in the set

#Pop function to remove elements randomly [from the end]
my_set.pop()
print(my_set)

#Clear function to clear all teh elements in the set
my_set.clear()
print(my_set)

# Delete function to del the set
# del my_set
# print(my_set)

my_set_2={1, 3, "ABC..."}
print(my_set_2)

# To Convert list in set
my_list=[1,2,3,5]
print((my_list))
my_set_3=set(my_list)

print(my_set_3)

# UNIION | INTERSECTION | DIFF | SYMMETRIC DIFF
A={"A", "B", 1, 4}
B={"B", "C",1, 7, 3}

# A UNION B
print(A.union(B))
print(A | B) # with symbol

# A INTERSECTION B
print(A.intersection(B))
print(A & B) # with symbol

# A DIFFERENCE B
print(A - B) # with symbol
print(A.difference(B))

# A Symmetric Difference B
print(A.symmetric_difference(B))
print(A ^ B) # With Symbol [only unique values will be printed]