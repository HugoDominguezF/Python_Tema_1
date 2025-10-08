class CuentaCorriente:

    def __init__(self,dni,nombre,saldo):
        self.DNI = dni
        self.nombre = nombre
        self.saldo = saldo

    def __init__(self,dni,saldo):
        self.DNI = dni
        self.saldo = saldo

    def sacarDinero(self,dinero):
        if self.saldo>=dinero and dinero >0 :
            self.saldo -= dinero
            sePudo = True
        else:
            sePudo = False
        return sePudo
    
    def ingresarDinero(self,dinero):
        if(dinero>0):
            self.saldo += dinero
    

    def __str__(self):
        return str(self.DNI+' tiene '+self.saldo+' euros')
    
    def __eq__(self, value):
        return self.DNI==value.dni
    
    def __lt__(self,value):
        return self.saldo<value.saldo
    