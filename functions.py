def speak(firstname, surname):
    print(f"Hello {firstname},{surname}")
speak ("Ryan", "Wright")


def shout(greeting, name):
    gup = str(greeting).upper()
    nup = str(name).upper()
    return f"{gup} + {nup}!"

print(shout("hi", "DFESW13"))
