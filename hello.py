import random

Caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lunghezza = int(input("Quanti caratteri deve avere la password? "))
password = ""

for i in range(lunghezza):
    password += random.choice(Caratteri)

print("La tua password è:", password)

