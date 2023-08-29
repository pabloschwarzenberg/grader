class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo
    
    
    def girar(self, giro):
        if giro <= self.saldo:
            self.saldo -= giro
            print("Se realizo el giro")
            return True
        else:
            print("No puede realizar un giro por ese monto")
        return False  
