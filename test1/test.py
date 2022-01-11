import random

secret = random.randint(0,10)
life = 3

print(secret)
nb = int(input("Rentrez un nombre svp : "))

while True:
    if nb == secret:
        print("GG !")
        exit(1)
    elif life == 0:
        print("Game Over L")
        exit(1)
    else:
        nb = int(input("Rentrez un nombre svp : "))
        life -= 1

#make a class with this add difficulty lvl 1 - 2 -3 
