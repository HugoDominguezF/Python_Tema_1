class Articulo:

    IVA = 21

    def __init__(self,nombre,precio,cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.cuantosQuedan = cuantosQuedan

    def getPVP(self):
        return self.precio+(self.precio*self.IVA)
    
    def getPVPDescuento(self,descuento):
        if descuento<101 and descuento>0:
            conDescuento = (self.precio+(self.precio*self.IVA)*((100-descuento)/100))
        return conDescuento
    
    def vender(self,cantidad):
        if self.cuantosQuedan >= cantidad and cantidad>0:
            self.cuantosQuedan -= cantidad
            sePudo = True
        else:
            sePudo = False
        return sePudo

    def almacenar(self,cantidad):
        if cantidad>0:
            self.cuantosQuedan+=cantidad
        

    def __str__(self):
        return f"El articulo {self.nombre} que cuesta {self.precio} tiene un stock de {self.cuantosQuedan}"
    
    def __eq__(self, value):
        return (self.nombre==value.nombre)
    
    def __lt__(self,value):
        return self.nombre<value.nombre
    