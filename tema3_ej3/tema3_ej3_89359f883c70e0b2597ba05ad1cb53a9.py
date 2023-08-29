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
    cuenta = CuentaCorriente("123456789", 1000)
    print("Saldo inicial:", cuenta.saldo)

    if cuenta.girar(500):
        print("Giro realizado.")
    else:
        print("No se puede realizar el giro.")

    print("Saldo actual:", cuenta.saldo)

    if cuenta.girar(800):
        print("Giro realizado.")
    else:
        print("No se puede realizar el giro.")

    print("Saldo actual:", cuenta.saldo)
           