class Cuenta:
    saldo = 0
    rut = ''
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo
        
    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto 
            return True
        else:
            return False   