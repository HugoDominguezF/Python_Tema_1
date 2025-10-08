
frase = input('Escribe una frase: ')

diccionario = {}

for palabras in range(len(frase)) :
    diccionario[frase[palabras]] = 1+int(diccionario.get(frase[palabras],0))

print(diccionario)