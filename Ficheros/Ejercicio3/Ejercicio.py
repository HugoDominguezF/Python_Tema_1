nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")

with open("Ficheros\\Ejercicio3\\datos.txt", "a") as fichero:
    fichero.write(f"{nombre} {edad}\n")
