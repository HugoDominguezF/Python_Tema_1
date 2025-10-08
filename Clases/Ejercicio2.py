class Libro:

    def __init__(self,titulo,autor,ejemplares,ejemplaresPrestados):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.ejemplaresPrestados = ejemplaresPrestados

    def prestamo(self):
        if self.ejemplares>0 :
            self.ejemplares -= 1
            self.ejemplaresPrestados +=1
            sePudo = True
        else:
            sePudo = False
        return sePudo
    
    def devolucion(self):
        if self.ejemplaresPrestados>0 :
            self.ejemplaresPrestados -= 1
            self.ejemplares +=1
            sePudo = True
        else:
            sePudo = False
        return sePudo
    

    def __str__(self):
        return str(self.titulo+' escrito por '+self.autor)
    
    def __eq__(self, value):
        return (self.titulo==value.titulo and self.autor==value.autor)
    
    def __lt__(self,value):
        return self.autor<value.autor
    