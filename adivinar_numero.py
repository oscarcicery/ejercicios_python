'''juego de adivinar el numero'''
import random

aleatorio= random.randint(1,1000)
'''print(aleatorio)'''
cont=0


while cont==0:
    numero = int(input("ingrese un numero entre 1 y 1000"))
    if numero<1 or numero>1000:
        while numero<1 or numero>1000:
            numero= int(input("Ey, ingrese un numero entre 1 y 1000"))

    if numero>aleatorio:
            print("el numero que ingresó es mayor al numero correcto")

    if numero < aleatorio:
                print("el numero que ingresó es menor al numero correcto")

    if numero == aleatorio:
            print("felicidades, adivinó el numero")
            cont = 1
            break
