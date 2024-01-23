# Print function :
# print("hello world")
# print("Day-1 Print python function")
# print("The function decleared like this:")
# print("print('what to print')")

# String Manipilatiion :
# print("Hello World!\nHello World!\nHello World!")

# for i in range(100):
#   print("Hello World!\n")

# print("Hello"+ " "+ "Parba")

# Input function :
# input("what is your name?")

# print("Hello" + input("what is your name?"))

# Length function (this is used to calculate the length of the string) :
# print(len(input("what is your name?")))

# Variables :
# name=input("what is your name?")
# print(name)

# name="Parba"
# print(name)

# name=input("what is your name?")
# length=len(name)
# print(length)

#exercies...
# a = input("a:")
# b = input("b:")
# c=a
# a=b
# b=c
# print("a:"+a)
# print("b:"+b)

# a = input("a:")
# b = input("b:")
# a, b = b, a
# print("a:"+a)
# print("b:"+b)

#Variable naming :
# user_name=input("what is your name?")
# length=len(user_name)
# print(length)

# 1st Project(Band Name Generator) :
# print("Welcome to the Band Name Generator.")
# city_name=input("What's name of the city you grew up in?\n")
# pet_name=input("What's your pet's name?\n")
# print("Your band name could be: "+" "+city_name+" "+pet_name)

# Data type :

# string :
# print("Hello"[0])
# print("Hello"[4])
# for i in range(4):
#   print("Hello"[i])

# print("123"+"456")

# print("Hello"+"World")

# Integer :
# print(123+456)

# Float :
# print (123.456)

# Boolean :
# True
# False

# TypeError :
# num_char = len(input("what is your name?"))
# print("Your name has" + num_char + "characters")

# Type checking :
# print(type(len(input("what is your name?"))))

# Type Converstion :
# num_char = len(input("what is your name?"))
# new_num_char = str(num_char)
# print("Your name has"+" "+ new_num_char +" "+"characters")

#if convert string to integer :
# num_char = len(input("what is your name?"))
# new_num_char = str(int(num_char))
# print("Your name has"+" "+ new_num_char +" "+"characters")

# #if convert string to float :
# num_char = len(input("what is your name?"))
# new_num_char = str(float(num_char))
# print("Your name has"+" "+ new_num_char +" "+"characters")

# #if convert string to bool :
# num_char = len(input("what is your name?"))
# new_num_char = str(bool(num_char))
# print("Your name has"+" "+ new_num_char +" "+"characters")

#Exercise:

# first = input("enter your first digit: ")
# second = input("enter your second digit: ")
# result =int(first) +int(second)
# print ("result:" + str(result))

# first_digit = input("two_digit_number[0]")
# second_digit = input("two_digit_number[1]")
# result = int(first_digit) + int(second_digit)
# print(result)

# Mathematical Operations :
# print(3+5)
# print(7-4)
# print(3*2)
# print(6/3)
# print(2**3)

# PEMDASLR :
#  ()  ~ Parentheses
#  **  ~ Exponents
#  *   ~ Multiplication
#  /   ~ Division
#  +   ~ Addition
#  -   ~ Subtraction

# 2nd Project (BMI Calculator) :
# weight = input("enter your weight in kg:")
# height = input("enter your height in m:" )
# BMI = int(weight) / float(height)**2
# print("BMI:" + str(int(BMI)))

# Number Manipulation :
# print(8/3)
# print (round(8/3))
# print (round(8/3,2))
# print (round(2.66666666,2))
# print (8//3)

# score = 0
# score += 1
# print(score)

# score = -2
# score -= 6
# print(score)

# F-String :
# score = 0
# height = 1.8
# iswinning = True
# print(f"your score is {score}, your height is {height}, you are winning is {iswinning} ")

# 3rd Project (Life in weeks) :

# age =input("what is your current age?")
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining =years_remaining * 52
# months_remaining =years_remaining * 12
# message = f"You have{days_remaining} days,{weeks_remaining} weeks,{months_remaining} months "
# print(message)

# 4th Project (Tip Calculator) :

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? Tk"))
# tip = int(input("What percentage tip would you like to give? 10,12, or 15?"))
# pepole = int(input("How many pepole to split the bill?"))
# bill_with_tip = tip / 100 * bill + bill
# print(f"Bill with tip : Tk {bill_with_tip}")
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / pepole
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay Tk {final_amount}")

# Control Flow with if/else :
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# if height >= 120:
#     print("You can ride the rollercoaster!")

# else:
#     print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators :
# > ~ Greater than
# < ~ Less than
# >= ~ Greater than or equal to
# <= ~ Less than or equal to
# == ~ Equal to
# != ~ Not equal to

# Odd or Even :
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#    print("This is an even number.")
# else:
#     print("This is an odd number.")

# Nested if/else :
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age <= 18:
#       print("Please pay 50 Tk.")
#     else:
#       print("Please pay 80 Tk.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# if/elif/else with Multiple if :
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#       bill = 30  
#       print("Child tickets are 30 Tk.")
#     elif age <= 18:
#       bill = 50  
#       print("Youth tickets are 50 Tk.")
#     elif age >= 45 and age <= 55: 
#       print("Everything is going to be ok. Have a free ride on us!.")    
#     else:
#       bill = 80  
#       print("Adult tickets are 80 Tk.")
    
#     wants_photo = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#       bill += 3
#     print(f"Your total bill is {bill} TK.")  
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# 5th project (BMI Calculator 2.0):
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# BMI = round(weight / height**2)
# if BMI < 18.5:
#   print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#   print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30:
#   print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35:
#   print(f"Your BMI is {BMI}, you are obese.")
# else:
#   print(f"Your BMI is {BMI}, you are clinically obese.")

# 6th project (Leap Year) :
# year = int(input("Which year do you want to check?"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year.")
#         else :
#             print("Not Leap Year.")          
#     else:
#         # print("Leap Year.")      
# else:
#     print("Not Leap Year.")

# 7th project (Pizza Order):
# print("Welcome to Python Pizza Deliveries!")
# size = input("What the size of pizza do you want? S,M or L.")
# add_pepperoni = input("Do you want pepperoni? Y or N.")
# extra_cheese = input("Do you want extra cheese? Y or N.")
# bill = 0
# if size == "S":
#     bill = 70 
# elif size == "M":
#     bill = 100
# else:
#     bill = 150

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 5
#     else:
#         bill += 7

# if extra_cheese == "Y":
#     bill += 3
    
# print(f"Your final bill is {bill}Tk")

# 8th project (Love Calculator) :
print ("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_strings = name1 + name2
lower_case_strings = combined_strings.lower()
t = lower_case_strings.count("t")
r = lower_case_strings.count("r")
u = lower_case_strings.count("u")
e = lower_case_strings.count("e")
true = t + r + u + e

l = lower_case_strings.count("l")
o = lower_case_strings.count("o")
v = lower_case_strings.count("v")
e = lower_case_strings.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90 :
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50 :
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")








# print ('''
# *******************************************************************************
#  _________|________________.=""_;=.______________|_____________________|_______
#                     |  ,-"_,=""     `"=.|                  |
#  ___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
#                     |    __.--" , ; `"=._o." ,-"""-._ ".   |
#  ___________________|_._"  $@!oo @!&$ ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._`!()oo @!()@  ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._.&$@.& ()$%-'o. "-._ /_______________|_______
#                     | |o;    `"-.o`"=._!@%()@'% ,__.--o;   |
#  ___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')
# print("Wlcome to Treasure Island!")
# print("Your mission is to find the treasure!")
# choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

# if choice1 == "left":
#     input('You\'ve come to a lake. There is an island in the niddle of the lake . Type "wait" to wait for a boat. Type "swim" to swim across.')
# else:
#     print("You fell into a hole. Game Over!")    