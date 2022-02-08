name = "Ryan Wright"

name[5] = "i"
print(name[2:8])

animal = "fox", "rabbit", "dog", "cat"

animal1, animal2, animal3, animal4 = animals
#we can assign the tuble values to variables as tuble lenghth will not change

print(animals)
print(animal2)
#returns rabbit


#DICTIONARIES
noises = {"cow":"moo", "sheep":"baa","Owen Wilson":"Wow"}

print(noises["Owen Wilson"])
#returns Wow

#How to add to dictionary
noises ["big car man"] = "Vroom vroom"

print(noises)
noises ["sheep"] = "Speak English"
print(noises)

print(list(noises.keys()))
#returns values
print(list(noises.items()))
#returns tuples containing key value pairs eg('cow', 'moo'), ('sheep,

print ("moo" in noises)
#returns false
print ("moo" in noises.values())
#returns true

my_words = {"hello": "hola", "thank you": "gracias"}
#get used to teruen value if key in dictionary
print(my_words.pop("thank you"))
print(my_words)
#return {'hello':hola'}

#we can use .update() to all to our list or update values for a key
print(my_words)



