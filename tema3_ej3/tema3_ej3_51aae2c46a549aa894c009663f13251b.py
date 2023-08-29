# Cuenta Corriente en un Banco
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo
    
    def girar(self, giro):
        if self.saldo > giro:
            self.saldo = self.saldo - giro
            return True
        else:
            return False
    
    def __str__(self):
        return "Rut: " + str(self.rut) + " / Saldo: " + str(self.saldo)