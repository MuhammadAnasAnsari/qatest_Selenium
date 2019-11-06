# Syntax dict{K:V}  unordered | changeable | no duplicate | indexed

my_dic = {
    "class": "Animal",
    "name": "Girrafe",
    "age": 10
}

print(my_dic)
print(my_dic["name"])  # to get the specific value of Dic.
print(my_dic.get("age"))  # to get the specific value of Dic. with get() func.
print(my_dic.values())  # to print all the values of dic

for x in my_dic:
    print(x)
    print(my_dic[x])  # To print all the values of the Dic.

# for x, y in my_dic:  # Error not using items(), "for x, y in my_dic:   ValueError: too many values to unpack (expected 2) "
#     print(x, y)  # To print the keys nd values of the Dic.


for x, y in my_dic.items():  # Items() use to print keys and values [Valid]
    print(x, y)  # To print the keys nd values of the Dic.

# To change the any key value in the Dic.
my_dic["name"]="Elephant"
print(my_dic)

# to Add new Key and its value in the Dic.
my_dic["Color"]="Black"
print(my_dic)

#  Pop any key
my_dic.pop("Color")
print(my_dic)

#popitem() to delete the last item from the Dic.
my_dic.popitem()
print(my_dic)

# Del to delete the object from the Dic
del my_dic["class"]
print(my_dic)

#Clear Everything from the Dic
my_dic.clear()
print(my_dic)

# to Delete the entire Dic
del my_dic
print(my_dic) # NameError: name 'my_dic' is not defined because Dic is deleted.