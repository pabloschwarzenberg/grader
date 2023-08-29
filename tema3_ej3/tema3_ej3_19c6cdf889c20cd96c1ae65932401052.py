# completa el código de la función
class Cuenta:
  pass
class Cuenta:
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
    cuenta = Cuenta("12345678-9", 50000)
    print(cuenta.girar(20000))  # True
    print(cuenta.saldo)  # 30000
    print(cuenta.girar(40000))  # True
    print(cuenta.saldo)  # -10000
    print(cuenta.girar(5000))  # False
    print(cuenta.saldo)  # -10000           