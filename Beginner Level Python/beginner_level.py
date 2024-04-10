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



# Exercies :
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



# if convert string to integer :

# num_char = len(input("what is your name?"))
# new_num_char = str(int(num_char))
# print("Your name has"+" "+ new_num_char +" "+"characters")



# if convert string to float :

# num_char = len(input("what is your name?"))
# new_num_char = str(float(num_char))
# print("Your name has"+" "+ new_num_char +" "+"characters")



# if convert string to bool :

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


   
# Random Module :

# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_float = random.random() * 5 
# print(random_float)



# Exercise (Heads or Tails) :

# import random
# random_side = random.randint(0,1)
# if random_side == 1:
#     print ("Heads")
# else:
#     print("Tails")



# List :

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]

# print(states_of_bangladesh[-2])
# print(states_of_bangladesh[-1])
# print(states_of_bangladesh[0])
# print(states_of_bangladesh[1])
# print(states_of_bangladesh[2])

# states_of_bangladesh[1] = "Chittagong"
# print(states_of_bangladesh)

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# states_of_bangladesh.append("Noakhali")
# states_of_bangladesh.extend(["Dinajpur","Cumilla"])
# states_of_bangladesh.insert(1,"Cumilla")
# states_of_bangladesh.remove("Mymensingh")
# print(states_of_bangladesh)

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# # removed_state = states_of_bangladesh.pop(2)
# print(states_of_bangladesh)
# print(f"Removed element: {removed_state}")

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# states_of_bangladesh.clear()
# print(states_of_bangladesh)

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# index_of_Rajshahi = states_of_bangladesh.index("Rajshahi")
# print(f"Index of 'Rajshahi': {index_of_Rajshahi}")

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# count_of_dhaka = states_of_bangladesh.count("Dhaka")
# print(f"Count of 'Dhaka': {count_of_dhaka}")

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# states_of_bangladesh.sort()
# print(states_of_bangladesh)
# states_of_bangladesh.sort(reverse=True)
# print(states_of_bangladesh)
# states_of_bangladesh.sort(reverse=False)
# print(states_of_bangladesh)

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# sorted_list = sorted(states_of_bangladesh)
# print(sorted_list)
# print(states_of_bangladesh)  # Original list remains unchanged

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# states_of_bangladesh.reverse()
# print(states_of_bangladesh)

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# copy_of_states = states_of_bangladesh[:]
# print(copy_of_states)



# Exercies (Banker Roulette - Who will pay the bill) :

# names_string = input("Give me everybody's names, seperated by a comma.\n")
# names = names_string.split(", ")
# num_items =(len(names))
# import random
# random_choice = random.randint(0, num_items-1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " is going to buy the meal today!")

# Otherwise...
# person_who_will_pay = random.choice(names)
# print(person_who_will_pay + " is going to buy the meal today!")



# Nested List :

# states_of_bangladesh = ["Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh", "Sylhet"]
# east = ["Dhaka","Chattogram"]
# west =["Rajshahi","Khulna"]
# north =["Barisal"]
# south = ["Rangpur","Mymensingh","Sylhet"]
# states_of_bangladesh = [east, west, north, south]
# print(states_of_bangladesh)



# Exercise (Treasure Map) :

# row1 = ["🐸","🤡","👹"]
# row2 = ["👺","👻","👽"]
# row3 = ["👾","🗿","💀"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure?")
# horizonal = int(position[0])
# vertical = int(position[1])
# selected_row = (map [vertical-1])
# selected_row[horizonal-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")



# for Loops with list :

# fruits = ["Apple", "Peach", "Pear"]
# print(fruits)
# for fruit in fruits:
#     #print(fruit)
#     print(fruit + " Pie")
#     #print(fruits)
    



# Exercise (Average Height) :

# student_heights = input("Input a list of student heights ").split(",")
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(number_of_students)     
 
# average_height = round(total_height / number_of_students)
# print(average_height)



# Exercise (High Score) :

# student_scores = input("Input a list of student scores ").split()
# lowest_score = int(input("put the test scope: "))
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0 
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}") 

# for score in student_scores:
#     if score < lowest_score:
#         lowest_score = score
# print(f"The lowest score in the class is:{lowest_score}") 
       
# lowest_score = float('inf')  # Initialize with positive infinity to ensure any score is lower
# for score in student_scores:
#     if score < lowest_score:
#         lowest_score = score
# print(f"The lowest score in the class is: {lowest_score}")



# for loop with range() function :

# for number in range(1, 11):
#     print(number)
# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range (1,101):
#     total += number
# print(total)    



# Exercise (Adding even Numbers) :

# total = 0
# for number in range(2,101,2):
#     total += number
# print(total)

# total2 = 0
# for number in range(1,101):
#     if number % 2 == 0:
#      total2 += number
# print(total2)     



# Exercise (The FizzBuzz Game ) :

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")        
#     else:
#         print(number)    



# # Defining Functions :  Define a function with the def keyword, then write the function identifier (name) followed by parentheses and a colon.

# def my_function() :
#     print("Hello")
#     print("Bye")

# # Calling The Function :   Type the name of the function followed by parentheses (). 

# my_function() 



# # Indentetion  :    Refers to the spaces at the beginning of a code line.

# def my_function():
#     if sky == "clear":
#         print("blue")
#     elif sky == "cloudy":
#         print("grey")
#     print("Hello")
# print("World")            



# # While Loop :    A control flow statement which repeatedly executes a block of code until the condition is satisfied. 

# while something_is_true:
#     #do this
#     #then do this
#     #finaly do this



# Better explanation between while & for loop :

# i = 0
# while i<= 6 :
#     print("hello"+str(i))
#     i += 1

# i = 0
# for i in range (6):
#     print("hello"+str(i))
#     i += 1



# Functions with Inputs :

# def greet():                          #simple functions
#     print("Hello Parba")
#     print("Good Morning Coder")
#     print("Best Wishs")
# greet()    

# def greet_with_name (name):            # function with inputs
#     #      ^           ^
#     #      |           |     
#     #      |           |      
#     #      |           |
#     # [Parameter]   [Argument]    

#     print(f"Hello {name}")
#     print(f"Good Morning {name}")
# greet_with_name("Parba")    

# # Functions with more than 1 Inputs :

#         #     [positional argument]
#         # -----------------------------
# def greet_with(name, location):        
#     print(f"Hello {name}")
#     print(f"What is it like in location {location}")
# greet_with("Parba", "Chattogram")    

#         #     [keyword argument]
#         # -----------------------------
# def greet_with(name, location):        
#     print(f"Hello {name}")
#     print(f"What is it like in location {location}")
# greet_with(name="Parba", location="Chattogram")         
# greet_with(location="Chattogram", name="Parba")   



#Exercise (Paint Area Calculator):
# import math
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area / cover)    #round up the number by using [math.cei:()]
#     print(f"You'll need {num_of_cans} cans of paint. ")

# test_h = int(input("Height of wall: "))
# tes_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=tes_w, cover=coverage)



#Exercise (Prime Number Checker):
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False       
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number")        

# n = int(input("Check this number: "))
# prime_checker(number=n)



# Dictionary {Key: Value} :      A kind of data structure that stores items in key-value pairs. Dictionary items are ordered, changeable, and do not allow duplicates.

# programming_dictionary = {
#     "Bug":"An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over & over again."
# }

# print(programming_dictionary["Bug"])   #retrieving items from dictinary.

# print(programming_dictionary["Bog"])     #wrong
# print(programming_dictionary[Bug])       #wrong

# programming_dictionary["Loop"] = "The action of doing something over & over again."         #adding new items to dictionary.
# print(programming_dictionary)

# empty_dictionary = {}       #creat an empty dictionary.

# programming_dictionary = {}         #wipe an existing dictionary.
# print(programming_dictionary)

# programming_dictionary["Bug"] = "A moth in your computer"       #edit an item in a dictinary. 
# print(programming_dictionary)

# for key in programming_dictionary:      #loop through a dictionary.
#     print(key)
#     print(programming_dictionary[key])



#Exercise (Grading Program) :

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades) 



#Nesting Lists in Dictionary :

# capitals = {                         #nesting.
#     "Bangladesh": "Dhaka",
#     "India": "Delhi",
# }

# travel_log = {                      #nesting a list in a dictonary.
#     "Bangladesh": ["Dhaka","Chottagram","Cumilla"],
#     "India": ["Delhi","Panjab","Bihar"],
# }

# travel_log = {                      #nesting dictonary in a dictonary.
#     "Bangladesh":{"cities_visited": ["Dhaka","Chottagram","Cumilla"],"total_visits": 7},
#     "India": {"cities_visited": ["Delhi","Panjab","Bihar"],"total_visits": 10},
# }

# travel_log = {                      #nesting dictionary in a list.
#     {
#     "country": "Bangladesh",
#     "cities_visited": ["Dhaka","Chottagram","Cumilla"],
#     "total_visits": 7
#     },
#     {                                                           #2 item & each item is a dictionary...
#     "country": "India",
#     "cities_visited": ["Delhi","Panjab","Bihar"],
#     "total_visits": 10
#     },
# }                      



#Exercise (Dictionary in list) :
                
# travel_log = [
#     {
#     "country": "Bangladesh",
#     "cities": ["Dhaka","Chottagram","Cumilla"],
#     "visits": 7
#     },
#     {                                                           #2 item & each item is a dictionary...
#     "country": "India",
#     "cities": ["Delhi","Panjab","Bihar"],
#     "visits": 10
#     },
# ]

# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["cities"] = cities_visited
#     new_country["visits"] = times_visited
#     travel_log.append(new_country)

# add_new_country("Russia",2,["Moscow", "Saint Petersbu"])
# print(travel_log)



# Docstring :       A string used to document a Python module, class, function or method.

          #function with outputs...
    # _________________________________        

# def formatted_name(f_name, l_name):
#     """Take a first and last name and format it to return the title case version of the name. """                      #this line example of the docstring !
#     if f_name == "" or l_name == "":                                                                     
#         return "You didn't provide valid input."                #___________________________________________       
#     formatted_f_name = f_name.title()                                                                   #   \        
#     formatted_l_name = l_name.title()        # (title function do the first word turn into capital word)  #  ------------------  This is called the multiple return values !            
#     return f"Result: {formatted_f_name} {formatted_l_name}"       #__________________________________________/  

# print(formatted_name(input("What is your first name?"),input("What is your last name?")))



#Exercise(Days in Month):

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     month_days = [31,28,31,30,31,30,31,31,30,31,30,31]  
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]

# year = int(input("Enter a year: "))    
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)



# Scope :

# enemies = 1 

# def increase_enemies():
#     enemies = 2 
#     print(f" enemies inside function {enemies}")

# increase_enemies()
# print(f"enemies outside function {enemies}")

# # # Local Scope :

# def drink_potion():
#     poition_strength = 2
#     print(poition_strength)

# drink_potion()
# print(poition_strenth)        # when want to print outside the function, gives error. 

# # Global Scope :
# player_health = 10

# def drink_potion():
#     poition_strength = 2
#     print(poition_strength)

# drink_potion()
# print(player_health)    

# player_health = 10

#if nested this function:

# player_health = 10

# def game():
#     def drink_potion():
#         poition_strength = 2
#         print(poition_strength)

#     drink_potion()
# game()
# print(player_health)    



# There is no block scope:              there are no function,that's why we can call there is no block scope!

# game_level = 3

# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)



# Modifying Global Scope :

# enemies = 1
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")



# Global Constant :     used to modify a global variable in a local context! 

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@ROY_PORBO"

# def calc():
#     PI



############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):      #   for i in range(1, 21): 
#     if i == 20:               #   if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)                              # dice_num = randint(0, 5)                
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")                      
# elif year > 1994:                                     # elif year >= 1994:  
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")                       # age = int(input("How old are you?"))
# if age > 18:                                      
# print("You can drive at age {age}.")                  # print(f"You can drive at age {age}.")                

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))            # word_per_page = int(input("Number of words per page: "))  
# total_words = pages * word_per_page                                                      
                                                                       # print(f"pages = {pages}") 
                                                                       # print(f"word_per_page = {word_per_page}")
                                                                       
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)             #just indent this line solveddd.....!
#   print(b_list)

# mutate([1,2,3,5,8,13])


