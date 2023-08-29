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
    cuenta_1 = CuentaCorriente("12864303-6", 10000)

    # Realizar giros
    print(cuenta_1.girar(2000))  # True
    print(cuenta_1.saldo)  # 8000

    print(cuenta_1.girar(12000))  # False
    print(cuenta_1.saldo)  # 8000

    cuenta_2 = CuentaCorriente("98765432-1", 5000)
    print(cuenta_2.girar(3000))  # True
    print(cuenta_2.saldo)  # 2000
