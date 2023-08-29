# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,quitar):
        if quitar<=self.saldo:
            print("Girando...")
            self.saldo=self.saldo - quitar
            print("Giro exitoso.")
            return True
        else:
            print("Monto insuficiente")
        return False