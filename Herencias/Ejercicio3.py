class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular(self, cantidad):
        return self.precio * cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio:.2f}"

    def __lt__(self, other):
        return self.precio < other.precio


class Perecedero(Producto):
    def __init__(self, nombre, precio, dias_a_caducar):
        super().__init__(nombre, precio)
        self.dias_a_caducar = dias_a_caducar

    def calcular(self, cantidad):
        total = super().calcular(cantidad)
        if self.dias_a_caducar == 1:
            total /= 4
        elif self.dias_a_caducar == 2:
            total /= 3
        elif self.dias_a_caducar == 3:
            total /= 2
        return total

    def __str__(self):
        return f"Perecedero: {self.nombre}, Precio: {self.precio:.2f}, Días a caducar: {self.dias_a_caducar}"


class NoPerecedero(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def calcular(self, cantidad):
        return super().calcular(cantidad)

    def __str__(self):
        return f"No perecedero: {self.nombre}, Precio: {self.precio:.2f}, Tipo: {self.tipo}"


p1 = Producto("Pan", 1.5)
p2 = Perecedero("Leche", 2.0, 2)
p3 = NoPerecedero("Arroz", 1.2, "Grano")

print(p1)
print("Total:", p1.calcular(4))

print(p2)
print("Total:", p2.calcular(4))

print(p3)
print("Total:", p3.calcular(4))
