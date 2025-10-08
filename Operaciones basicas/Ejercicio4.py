
from random import Random
import math as Math

numeroSecreto = Random().randint(1, 100)
numeroIngresado = int(input("Adivina el numero secreto: "))

while numeroIngresado != numeroSecreto:
    if numeroIngresado < numeroSecreto:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")
    numeroIngresado = int(input("Intentalo de nuevo: "))

print("Felicidades, has adivinado el numero secreto")
