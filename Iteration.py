number = 0
while number < 5:
    print(number)
    number += 1

item = ["Tiawat", "Sunil", "Sebastian", "Nicholas", "Nabil", "Martin"]
for student in item:
    print(student)

for x in "DFESW13":
    print(x)

print(list(range(10)))
#range (stop)
#returns 0,1,2,2,3,4,5,6,7,8,9

print(list(range(4, 10)))
#range (start, stop)
#returns 4,5,6,7,8,9

my_words = {"hello": "hola", "thank you": "gracias", "yes": "si"}
for key in my_words:
    print(key)
#returns hello
#thank you
#yes

for value in my_words.values():
    print(value)

pydics = {"Name": "Ryan", "Age": 29, "Hungry": "Very"}
result = []

for x in pydics.values():
    result.append(x)
    print(result)


for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    for j in range(10):
        print(f'{j} * {i} = {j*i}')


