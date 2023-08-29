class CuentaCorriente:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo
    
    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
     else:
            return False

# Ejemplo de uso
cuenta = CuentaCorriente("123456789", 5000)
puede_girar = cuenta.girar(2000)
if puede_girar:
    print("Giro realizado. Saldo restante:", cuenta.saldo)
else:
    print("No se puede realizar el giro. Saldo insuficiente.")
           