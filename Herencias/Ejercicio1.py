class Animal:
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

    def habla(self):
        return ""

    def __str__(self):
        return f"Me llamo {self.nombre}, tengo {self.patas} patas y sueno asi: {self.habla()}"


class Gato(Animal):
    def habla(self):
        return "Miau"

    def __str__(self):
        return "Soy un gato. " + super().__str__()


class Perro(Animal):
    def habla(self):
        return "Guau"

    def __str__(self):
        return "Soy un perro. " + super().__str__()


# Ejemplo de uso
gato = Gato("Misu", 4)
perro = Perro("Rex", 4)

print(gato)
print(perro)