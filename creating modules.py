#boss.py

from boss import bad_boss

def good_boss(name):
    print(f"{name} is a good boss!")
    
def bad_boss(name):
    print(f"{name} is a bad boss!")

def not_a_boss(name):
    print(f"{name} is not even a boss!")

app.py:
import boss
boss.bad_boss("Bill Steves")
