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

# Ejemplo de uso:
if __name__ == "__main__":
    cuenta = CuentaCorriente("12345678-9", 1000)

    print(cuenta.saldo)  # Saldo inicial de la cuenta

    monto_giro = 500
    puede_girar = cuenta.girar(monto_giro)
    if puede_girar:
       print(f"Se realizó un giro de {monto_giro}")
    else:
        print("No se puede realizar el giro")

    print(cuenta.saldo)  # Saldo después del giro
