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
        if __name__ == "__main__":
    cuenta = CuentaCorriente("12345678-9", 10000)
    
    print(f"Saldo inicial: {cuenta.saldo}")
    
    if cuenta.girar(5000):
        print("Giro exitoso.")
    else:
        print("No se puede realizar el giro.")
    
    print(f"Saldo después del giro: {cuenta.saldo}")

