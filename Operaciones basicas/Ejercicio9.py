
def numeros_intermedios(param1, param2) :

    if(param1>param2):
        inicio = param2
    else:
        inicio = param1

    for contador in range(1, abs(param2-param1)):
        print(str(inicio+contador)+', ' ,end='')


numero1= int(input('Dime un numero: '))
numero2 = int(input('Otro numero: '))

numeros_intermedios(numero1,numero2)