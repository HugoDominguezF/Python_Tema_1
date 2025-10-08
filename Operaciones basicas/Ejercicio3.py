respuesta = int(input("Introduce un número (negativo para parar): "))

suma = 0

while respuesta >= 0:
    suma += respuesta
    respuesta = int(input("Introduce un número (negativo para parar): "))

print("La suma total de los números es " + str(suma))