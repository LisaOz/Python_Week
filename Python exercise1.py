#How to mark a comment

#How to get user input from the terminal
from csv import list_dialects
from tkinter.ttk import _TreeviewHeaderDict
from xmlrpc.client import Boolean


input("please tell me your name? ")

#How to print out to the terminal
print("Hello World")

#How to find out the data type
print(type(3.0))

attendance = 45
print(bool(attendance))

#syntax is important, spelling is important

name = "Ryan"

#str.lower() converts string to lower case
print(name.lower())
#str.upper () convert strink to upper case
print(name.upper())

#str. replace replaces old subscribing with new
print(name.replace("Wright", "lastname"))

#str.split() returns a list of words in the string we can specify the separator
print(name.split(","))

#str.join() concatenates an iterable or collection of strings
print(" join ".join(['Ryan', 'Paul', 'Wright']))

#str.count()returns number of non-overlapping occurences of substring in a string
print(name.count("a"))

#str.isdigit() Return true if string digital string, false otherwise
str1 = "Cat"
#returns false
str2 = "123"
#returns true
str3 = "12e4"
#returns false only accepts digits

print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())

#concationation combining strings together
print("dog" + "cat")
#returns dogcat
print("dog", "cat")
#returns dog cat

school = "High"
age = 49
math = True
testscore = 50.5

print("My name is", name, "My age is", age, "Maths", maths, "My testscore is", testscore)
#f strings allows us to combine multiply datatypes in a astring as well as perform calculation within curly brackets
print (f"My name is {name}, my age is {age}, my testscore is {testscore}")

print("Hello my name is \"ryan\"")
print('Hello my name is "ryan"')
#returns Hello my name is "ryan"
print('Hello my name is \\ryan\\') 
#returns Hello my name is \ryan\
print('Hello \t my name is ryan')
#returns Hello    my name is ryan


#TUTORIALs FROM QA


firstname = input("Lisa")
lastname = input("Frolova")
print("Hello","first name","lastname")


number1 = float(input("Please enter the first number: "))
number2 = float(input("Please  enter the second number: "))
answer = number1, "+" number2, "=", answer


#store input numbers 

number1 = input ("1")
number2 = input ("1.5")
print(number1, "+",  number2, "=", answer)

#add two numbers
sum = float(number1) + float(number2)

#display the sum
print ('the sum of {0} and {1}')


integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(10)
print(10,2)
?????

#What will be the output of this code?
Boolean
#pet
name = Pep Guardogiola
age = 3
bark = True
tweet = False

print(f"My pet is called", {name}, "he is", {age}, "years old.")
print("Statement:", name, "barks", bark)
print("Statement:", name, "tweets", tweet)













