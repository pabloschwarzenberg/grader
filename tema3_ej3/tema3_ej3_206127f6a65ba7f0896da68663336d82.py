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


if __name__ == "__main__":
    cuenta = CuentaCorriente("123456789-0", 1000)

    monto_giro = float(input("Ingrese el monto a girar: "))

    if cuenta.girar(monto_giro):
        print("Giro exitoso.")
    else:
        print("Saldo insuficiente.")
