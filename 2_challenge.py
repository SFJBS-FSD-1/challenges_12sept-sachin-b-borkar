# Challenge 1: Write a function that takes a natural number as input and outputs the number of digit in it.
# Conversion of number to string is not allowed

# user_input = int(input("enter a number"))
# def digits(user_input):
#     count = 0
#     while (user_input >0 ):
#         user_input = user_input //10
#         count  = count + 1
#     print(f"Number of digits is {count}")
# digits(user_input)


# Challenge 2: Write a function that takes a natural number as input and outputs the reverse of that number.
# Conversion of number to string is not allowed

# user_input= int(input("enter a number to be reversed: "))
# def reverse(user_input):
#     Reverse = 0
#     while(user_input > 0):
#         Reminder = user_input %10
#         Reverse = (Reverse *10) + Reminder
#         user_input = user_input //10
#     print(f"Reverse of entered number is {Reverse}")
# reverse(user_input)


# Challenge 3 : Write a function where user will enter a natural number as input and output returns the number of zeroes in the end of the factorial of that number.
# Conversion of number to string is not allowed

# def findZeros(n):
#     count = 0
#     while (n >= 5):
#         n //= 5
#         count = count + n
#     return count
#
# n = int(input("enter a number"))
# print("Count of  Zeros ", findZeros(n))

# Challenge 4 : list1 = ["India" , "England", "Spain"]list2 = ["Delhi","London","Madrid"]Write your own function that takes list1 and list2 as inputs and returns a dictionary like
# dict1 = {India” : “Delhi” , “England”:”London”, “Spain”:”Madrid”}

# list1 = ["India" , "England", "Spain"]
# list2 = ["Delhi","London","Madrid"]
# result = {}
# for key in list1:
#    for value in list2:
#       result[key] = value
#       list2.remove(value)
#       break
# print("Dictionary from lists ",result)

# Challenge 5 :Given places = {(“19.07'53.2”, “72.54'51.0”): "Mumbai", (“28.33'34.1”, “77.06'16.6”): "Delhi"}Write code to create a new dictionary using given dictionary
# city = {"Mumbai": “Latitude”: “19.07'53.2” , “Longitude”: “72.54'51.0”}, “Delhi” : {“Latitude”: “28.33'34.1” , “Longitude”: “77.06'16.6”}
places = {("a","b"): "Mumbai", ("x", "7"): "Delhi"}
city = {}
for key in places:
    for value in places:
        city[value] = key
        break
print(city)

# Challnege 6 : Given mylist = [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]Using for loop find the sum of all even numbers in mylist
# mylist = [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
# sum = 0
# for i in mylist:
#    if i %2 == 0:
#       sum = sum + i
#    else:
#          pass
# print(sum)
