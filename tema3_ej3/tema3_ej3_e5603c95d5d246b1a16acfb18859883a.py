class CuentaCorriente:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo
    
    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False


# Ejemplo de uso
cuenta = CuentaCorriente("123456789", 50000)

monto_giro = 20000
puede_girar = cuenta.girar(monto_giro)

if puede_girar:
    print("Giro realizado con éxito")
    print("Saldo actual:", cuenta.saldo)
else:
    print("No se puede realizar el giro. Saldo insuficiente.")
    print("Saldo actual:", cuenta.saldo)
