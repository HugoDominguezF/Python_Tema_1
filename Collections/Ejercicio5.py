
import random

lista = []



for contador in range(0,100):
    lista.append(random.randint(0,101))

print(lista)

numero = int(input('Dime un numero y te dire cuantas veces se repite: '))

veces = int(lista.count(numero))

print('El numero se repite '+str(veces)+' veces')