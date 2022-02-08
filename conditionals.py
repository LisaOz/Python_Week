my_boolean = True
my_boolean2 = True
if my_boolean:
    print("Both true")
else:
    print("First true 2nd False")
    print("Boolean is false")
#will return both true

my_money = 10
name = "Ryan"

if my_money < 10 or name == "Ryan":
    print("Get a job")
else:
    print("Nice")

deposit = 100
password = "password"

if 0 < deposit <= 100 and password == "password":
    print(f"Thank you for depositing {deposit}")
else:
    print("Failure")

name = "Root"
name1case = name.lower()

if name in ("Root", "admin"):
    print("Unacceptable username")
else:
    print(f"Welcome {name}")
    
age = int(input("gis your yer"))

if age >= 85:
    print("85 or older")
elif age >=65:
    print("Betweeb 65 and 85")
elif age >=45:
    print("Between 45 and 65")
elif age >=20:
    print("Between 20 and 45")
else:
    print ("Jelly or your youth")

