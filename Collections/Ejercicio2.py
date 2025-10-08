
lista = []

print('Agrega 10 numeros distintos')

for contador in range(1,11):
    lista.append(int(input('Siguiente numero: ')))

print('El numero maximo es '+str(max(lista))+' y el minimo es '+str(min(lista)))