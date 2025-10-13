with open("Ficheros\\Ejercicio4\\numeros.txt", "r") as fichero:
    numeros = [int(linea.strip()) for linea in fichero]

numeros.sort()

with open("Ficheros\\Ejercicio4\\numeros_ordenados.txt", "w") as fichero:
    for numero in numeros:
        fichero.write(f"{numero}\n")
