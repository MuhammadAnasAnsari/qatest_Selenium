# if 5 > 10:
#     print("5 is greater than 10")
# else:
#     print("5 is less than 10")
# ======================================
# Contional compare if,elif,else
# def compare():
#     if x >=z:
#         print("x>z", x > z, x)
#     elif y > z:
#         print("y>z", y > z, y)
#     elif z > (y + x):
#         print("z>(y+x)", z > (y + x), z)
#     else:
#         print("Failure...!")
#
#
# if __name__ == '__main__':
#     print("Enter number x:")
#     x = input()
#     print("Enter number y:")
#     y = input()
#     print("Enter number z:")
#     z = input()
#     print(compare())
# =============================================================
# print("Enter a number:")
# num = int(input())
# num=int(float(input())
# print(num)
# # if num> "0":
# if num> 0:
#     print("This is a positive number:", num)
# else:
#     print("This is negative number:", num)

# Find user entered negative or positive number
# def is_positive():
#     if num > 0:
#         print("You enter a positive number")
#     elif num == 0:
#         print("You enter Zero")
#     else:
#         print("You enter a negative number")
#
#
# if __name__ == "__main__":
#     print("Enter a number:")
#     num = float(input()) # to convert input string into float
#     is_positive()
# ===============================================================
# To FInd the total/Sum of the list
# def total():
#     num = [1, 2, 4, 6, 7, 9, 10, 23, 100]
#     sum = 0
#     for val in num:
#         sum = sum + val
#     print("Total is:", sum)
#
#
# if __name__ == '__main__':
#     total()
# ==================================================================
# to find the fruits in th bucket  If loop
# def fruits_bucket():
#     fruits=["Apple", "Orange", "Banana", "Peach"]
#     if val in fruits:
#         print("Apple is present in the Bucket :)")
#     else:
#         print(val + " is not present in the bucket :(")
#
#
# if __name__=='__main__':
#     print("Enter any fruit you want:")
#     val=input()
#     fruits_bucket()
# =====================================================================
# To see the fruits available? For loop
# def fruits():
#     fruits = ["Apple", "Orange", "Banana", "Peach", "Grapes"]
#     for val in fruits:
#         print(val)
#     else:
#         print("No fruit left :(")
#
#
# if __name__=='__main__':
#
#     fruits()

# ==================================================

# Find the sum of the first 10 numbers with While loop
# sum=0
# num=10
# i=1
# while num>=i:
#     sum = sum+i
#     i=i+1
# print("Sum is ", sum)

# ===================================================


def total():
    i = 1
    su = 0
    while num > i:
     su = su + i
     i = i + 1
    print("Sum is ", su)

if __name__ == '__main__':
    print("Enter a number: ")
    num = int(input())
    total()
