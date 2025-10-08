
def menu():
    print('1) Agregar nueva venta')
    print('2) Calcular total ventas')
    print('3) Salir')

diccionario = {}

menu()
respuesta=int(input())
while respuesta != 3:
    match respuesta:
        case 1:
            producto=input('¿Que venta quieres agregar?: ')
            diccionario[producto] = diccionario.get(producto, 0) +1
            print(diccionario)
        case 2:
            producto=input('¿Cual producto quieres calcular?')
            print(producto+' tiene un total de '+str(diccionario[producto])+' ventas')
        case _:
            print('No es una respuesta valida, ingrese otra vez la respuesta')
    menu()
    respuesta=int(input())
