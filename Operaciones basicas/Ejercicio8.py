numero = int(input("Dime un numero: "))

for pisos in range(1, numero+1):
    print(' ' * (numero - pisos), end='')
    for escalones in range(1, pisos+1):
        print('* ', end='')
    print()