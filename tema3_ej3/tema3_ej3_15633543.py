# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,giro):
        if giro > self.saldo:
            print("El giro que desea realizar es superior al saldo disponible.")
            return False
        elif giro <= self.saldo:
            self.saldo = self.saldo - giro
            return True
    def __repr__(self):
        return str(self.saldo)

           