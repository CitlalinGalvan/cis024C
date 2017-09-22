
# coding: utf-8

# # Exercise 1 - if statement
# 
# Write a python program to accept a number from the user. 
# Use the if statement to check to see if the number is 
# greater than 100. If the number is greater than 100, 
# print the message "Found a number greater than 100"

# In[1]:

num = input("Enter a number: ")

if num > 100:
    print "Found a number greater than 100"


# # Exercise 2 - if...else statement
# 
# Write a python program to accept the name of a user. 
# Use the if statement to check to see if the name is "Joe". 
# If the name is "Joe", print the message 
# "User Joe was entered", otherwise if the name is not "Joe", 
# print a message saying that "User Joe was not entered"

# In[6]:

name = raw_input("Enter user name: ")

if name == "Joe":
    print "User Joe was entered."
else:
    print "User Joe was not entered"


# # Exercise 3 - if..elif...else statement
# 
# Write a python program to accept the salary of the user.
# If the salary is less than 70,000, then print the message 
# "User salary is less than 70000", otherwise if the salary 
# is less than 100,000, print the message 
# "User salary is less than 100,000", otherwise, print the message 
# "User salary is greater than or equal to 100,000"

# In[8]:

salary = input("Enter your salary: ")

if salary < 70000:
    print "User salary is less than 70,000"
elif salary < 100000:
    print "User salary is less than 100,000"
else:
    print "User salary is greater than or equal to 100,000"


# # Exercise 4 - for loop
# 
# Write a program to get a number from the user. 
# Find the some of all numbers from 1 to the number 
# that the user entered.
# 
# For example, if the user enters 10, then you would need 
# to find the sum of all numbers from 1 to 10 like so. 
# Use the range statement in the for loop...
# see week 2 classwork for more information on the range statement
# 
# 1+2+3+4+5+6+7+8+9+10
# 
# Print the result

# In[28]:

numberSum = 0
num1 = input("Enter a number: ")

#create the sum of number 1 through given number
for number in range(1, num1+1):
    numberSum = numberSum + number
    
print "Range: ", range (1,num1+1)
print "Result is %s. " % (numberSum)


# # Exercise 5 - while loop
# 
# Guessing a number.
# 
# Initialize a variable called myNumber to any arbitrary value. 
# For example, maybe you thought of a number 9
# 
# Use the while loop to ask the user to enter a number. Check to see
# if the number entered by the user matches the number myNumber that
# you thought of. If there is a match, break from the while loop and
# print "Yippee! User guessed the right number". If there is no match
# allow the while loop to continue to ask the user for a number until 
# a match is found

# In[34]:

myNumber = 58

print "Please guess my number correctly."

guess = input("Enter a guess: ")
while guess != myNumber:
    guess = input ("Enter another guess: ")

print "Yippee! User guessed the right number"

