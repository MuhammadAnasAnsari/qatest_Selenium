print("Hello World....!")

# Variables Names case sensitive, use letters(a-z), underscore, numbers(0-9)
_x = 5
y = "Automation"
z = 0.5
G9 = 105.98j
print(type(_x), _x)  # to print the classes types of variables
print(type(y), y)
print(type(z), z)
print(type(G9), G9)
print("Hello " + y)

# maths operators
a = 100
b = 5
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Remainder =", a % b)

# Casting
f = int(6.5)  # 6
h = int(4)  # 4
j = float(45)  # 45.0
k = str(234)  # "234"

print(type(f), f)
print(type(h), h)
print(type(j), j)
print(type(k), k)

# strings operation
x = "Hello Ali"
y = "Bhai"
z= "Automation Selenium  "
print(x + " " + y)
print(x[4])  # To print 4th index value / alphabet
print(x[1:8])  # To print the index range
print(y.lower())  # To print the string in all lower case
print(x[6:9].upper())  # To print the string range in all upper case
print(z.split())       #To split the string
print(z.split(","))    #To split the string + remove "," sign
print(z[2:8].split())       #To split the string range

#Input
print("Whats your name? : ")
Answer=input()
print("Hello " + Answer +"!")