
import random

letras = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
diccionario = {}

for letra in letras:
    diccionario[letra] = random.randint(1, 101)

print(diccionario)