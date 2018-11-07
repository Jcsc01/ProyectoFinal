class Usuario():
    dni=''
    nombre=''
    saldo=0
    numero_cuenta=''
    def __init__(self,dni,nombre,apellido,saldo,numero_cuenta):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.saldo=saldo
        self.numero_cuenta=numero_cuenta
    
    def toString(self):
        return self.dni+" "+self.nombre+" "+self.apellido+" "+self.saldo+" "+self.numero_cuenta