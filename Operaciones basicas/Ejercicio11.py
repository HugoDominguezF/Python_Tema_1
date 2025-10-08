
def es_vocal(param1):
    vocales = ['a','e','i','o','u']

    if param1 in vocales:
        vocal=True
    else:
        vocal=False
    return vocal


letra = input('Dime una letra y te dire si es una vocal: ')

si_es = es_vocal(letra)

if(si_es):
    print('Si es una vocal')
else:
    print('No es una vocal')
