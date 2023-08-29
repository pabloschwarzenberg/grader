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
if __name__ == "__main__":
    cuenta = CuentaCorriente("12345678-9", 5000)
    print("Saldo inicial:", cuenta.saldo)
    
    monto_a_girar = int(input("Ingrese el monto a girar: "))
    if cuenta.girar(monto_a_girar):
        print("Giro realizado con éxito")
    else:
        print("No se puede realizar el giro. Saldo insuficiente")
    
    print("Saldo actual:", cuenta.saldo)