with open("Ficheros\\Ejercicio2\\mi_fichero.txt", "w") as fichero:
    while True:
        linea = input("Introduce una línea (o 'fin' para terminar): ")
        if linea.lower() == "fin":
            break
        fichero.write(linea + "\n")
