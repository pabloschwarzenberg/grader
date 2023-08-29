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
    cuenta1 = Cuenta("123456789", 1000)
    print(cuenta1.girar(500))  # Imprime: True (El giro se puede realizar)
    print(cuenta1.saldo)  # Imprime: 500 (El saldo se ha actualizado)

    print(cuenta1.girar(1000))  # Imprime: False (El giro no se puede realizar por saldo insuficiente)
    print(cuenta1.saldo)  # Imprime: 500 (El saldo no ha cambiado)
           