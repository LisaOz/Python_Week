# Create a new python file. in that file create a program that work out a grade based on marks with the use of fuctions.
# the program should take the students name, homework score (/25), assessment score (/50)
# and final exam score (/100) as inputs, out output their name and final ICT grade as a percentage.

#Stretch goal: include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

def grade(name, hwrk, asm, fes):
    f_percentage = ((hwrk + asm + fes)/175)*100
    if f_percentage > 100:
        return f"{name} use system correctly" 
    elif f_percentage > 85:
            return f"{name} your final course percentage is {f_percentage} Grade A*"
    elif f_percentage > 70:
        return f"{name} your final course percentage is {f_percentage} Grade A"
    elif f_percentage > 60:
        return f"{name} your final course percentage us {f_percentage} Grade B"
    elif f_percentage > 40:
        return f"{name} your final course percentage us {f_percentage} Grade D"
    else:
        return f"{name} your final course percentage us {f_percentage} Failed"
        

name_input = input ("Please enter your name: ")
hmwrk_input = int(input("Please enter your homework score (/25:"))
asm_input = int(input("Please enter your assessment score (/50):"))
fes_input = int(input("Please enter your final exam score (/100):"))

print(grade(name_input, hmwrk_input, asm_input, fes_input))