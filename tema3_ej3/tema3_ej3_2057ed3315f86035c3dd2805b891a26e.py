# completa el código de la función
class Cuenta:
  pass
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
    print(cuenta.girar(5000))  # True
    print(cuenta.saldo)  # 5000

    print(cuenta.girar(10000))  # False
    print(cuenta.saldo)  # 5000
           