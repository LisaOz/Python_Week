books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaiden's Tale"])

#Write a program which will do the following:
#Create a list which contains the first name of everyone in your cohort 
#and store it in a variable called team.
#Add your trainer to the list without manually editing it.
#Print the list to the terminal.
#Print only the 5th person in the list to your terminal.


team = {"Ryan", "Sebastian", "Baki", "Feruza"}
print 


#Exercise 2
#Ask for an input from the user as a mark
#if the mark is greater thatn 85 print "Distinction"
#if the mark is between 65 and 85 prinf "Pass"
#anything else iring "Fail"


exam = float(input("What is your exam mark: "))
print(exam)

if mark >= 85:
    print("Distinction")
elif mark >= 65:
    print("Pass")
else:
    print ("Fail")



    # Times Table Grid: 
    # #Given an integer n, write a python application 
    # #which returns a times table grid 
    # #for all the integers between 1 and n.
    # The grid should be separated by tabs and new lines.


n = int(input("Input a number: "))
line = ""
for row in range(1, n+1):
    for column in range(1, n+1):
        line = line +str(row*column) + "\t"
    line - line + "\n"

print(line)


#Write a while loop which asks for the names of 5 people,
# and for each person prints their name followed by the text "is awesome!"


