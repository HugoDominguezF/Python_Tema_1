def calculadora(param1,param2,operacion):

    match operacion :
        case 1:
            resultado = param1+param2
        case 2:
            resultado = param1-param2
        case 3:
            resultado = param1*param2
        case 4:
            resultado = param1/param2
        case _:
            resultado = 'Operacion no valida'
    return str(resultado)


numero1= int(input('Dime un numero: '))
numero2 = int(input('Otro numero: '))
print('1) Sumar')
print('2) Restar')
print('3) Multiplicar')
print('4) Dividir')
operar = int(input())

print(calculadora(numero1,numero2, operar))