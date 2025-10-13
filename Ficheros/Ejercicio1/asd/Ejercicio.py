
with open("Alumnos.txt", "r") as f:
    lineas = f.readlines()

nombres = []
edades = []
estaturas = []

for linea in lineas:
    partes = linea.strip().split()
    if len(partes) == 3:
        nombre = partes[0]
        edad = int(partes[1])
        estatura = float(partes[2])

        nombres.append(nombre)
        edades.append(edad)
        estaturas.append(estatura)

print("Nombres de los alumnos:")
for n in nombres:
    print("-", n)

media_edad = sum(edades) / len(edades)
media_estatura = sum(estaturas) / len(estaturas)

print(f"\nMedia de edad: {media_edad:.2f}")
print(f"Media de estatura: {media_estatura:.2f}")