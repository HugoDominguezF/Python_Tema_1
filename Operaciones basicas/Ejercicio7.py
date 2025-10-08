
numero = print("Dime un numero y te dire si es primo o no")
numero = int(input())
es_primo = True
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break
if es_primo and numero > 1:
    print("El numero " + str(numero) + " es primo")
else:
    print("El numero " + str(numero) + " no es primo")
