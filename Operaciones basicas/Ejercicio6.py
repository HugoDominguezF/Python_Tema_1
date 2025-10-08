
numero = int(input("Dime un numero: "))

contador = int(numero)
suma = 1

while contador > 1:

    suma *= contador
    contador -= 1

print(str(suma))