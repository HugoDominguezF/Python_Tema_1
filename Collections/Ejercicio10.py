
conjunto1 = ['e', 'i', 'k', 'm', 'p', 'q', 'r', 's', 't', 'u', 'v']
conjunto2 = ['p', 'v', 'i', 'u', 'm', 't', 'e', 'r', 'k', 'q', 's']


diccionario = dict(zip(conjunto1, conjunto2))

frase = input("Introduce una frase: ")

frase_encriptada = ""

for letra in frase:

    if letra in diccionario:
        frase_encriptada += diccionario[letra]
    else:

        frase_encriptada += letra


print("Frase encriptada:", frase_encriptada)