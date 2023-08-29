# completa el código de la función
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
    cuenta_1 = Cuenta("12864303-6", 10000)
    print(cuenta_1.girar(5000))  # True, el giro se puede realizar
    print(cuenta_1.saldo)  # 5000, el saldo se ha actualizado
    print(cuenta_1.girar(10000))  # False, el giro supera el saldo disponible
    print(cuenta_1.saldo)  # 5000, el saldo no se ha modificado
