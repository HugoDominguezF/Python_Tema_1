def numero_maximo(param1, param2) :

    if(param2>param1):
        max = param2
    else:
        max = param1
    print('El numero maximo es '+str(max))


numero1= int(input('Dime un numero: '))
numero2 = int(input('Otro numero: '))

numero_maximo(numero1,numero2)