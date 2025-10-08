
lista = []

print('Agrega 10 numeros distintos')

for contador in range(1,11):
    lista.append(int(input('Siguiente numero: ')))

lista.sort()
print(lista)