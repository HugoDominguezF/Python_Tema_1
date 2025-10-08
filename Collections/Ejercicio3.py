
lista = []



print('Agrega 8 numeros distintos')

for contador in range(1,9):
    lista.append(int(input('Siguiente numero: ')))

for contador in range(0,8):
    es_par = "par" if (int(lista[contador]) % 2 ==0) else "impar" 
    print(str(lista[contador])+':'+es_par+', ', end='')
