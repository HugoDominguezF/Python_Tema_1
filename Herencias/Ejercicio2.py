class Empleado:
    def __init__(self, nombre=""):
        self.__nombre = nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def __str__(self):
        return f"Empleado {self.__nombre}"


class Operario(Empleado):
    def __init__(self, nombre=""):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Operario"


class Directivo(Empleado):
    def __init__(self, nombre=""):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Directivo"


class Oficial(Operario):
    def __init__(self, nombre=""):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Oficial"


class Tecnico(Operario):
    def __init__(self, nombre=""):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Tecnico"

