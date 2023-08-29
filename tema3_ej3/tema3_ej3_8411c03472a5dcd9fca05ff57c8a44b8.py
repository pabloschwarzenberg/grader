# completa el código de la función
class Cuenta:
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
    cuenta = Cuenta("123456789", 10000)
    print(cuenta.girar(5000))  # True
    print(cuenta.girar(8000))  # False
    print(cuenta.saldo)  # 5000

           