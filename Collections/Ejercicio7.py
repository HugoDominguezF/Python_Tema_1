
def menu():
    print('1) Añadir contacto')
    print('2) Eliminar contacto')
    print('3) Buscar contacto')
    print('4) Salir')


diccionario = {}

menu()
respuesta=int(input())
while respuesta != 4:

    match respuesta:
        case 1:
            contacto = input('¿Que usuario quieres añadir?')
            telefono = input('¿Que telefono le quieres añadir?')
            diccionario[contacto] = telefono
        case 2:
            eliminar = input('¿Que usuario quieres eliminar?')
            del diccionario[eliminar]
        case 3:
            buscar = input('¿Que usuario quieres buscar?')
            if buscar in diccionario:
                print(buscar+' : '+diccionario[buscar])
            else:
                print('No se ha encontrado el usuario')
        case _:
            print('Opcion no valida')

    menu()
    respuesta = int(input())