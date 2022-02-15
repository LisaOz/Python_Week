class Dog:
    number_of_legs = 4
    breed = "Springter"
    furcolour = "Black"

    def speak(self):
        print("Woof")

bilbo_waggins = Dog()
betsy = Dog()
fido = Dog()
jeff = Dog ()

bilbo_waggins.speak()
print(bilbo_waggins.breed)

bilbo_waggins.breed = "German Sheppard" <-- we can change object attribute
