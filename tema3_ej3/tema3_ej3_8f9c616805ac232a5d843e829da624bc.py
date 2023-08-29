class CuentaCorriente:
    def __init__(self, saldo):
        self.saldo = saldo

    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False


# Ejemplo de uso
if __name__ == "__main__":
    cuenta = CuentaCorriente(1000)
    print(cuenta.girar(500))  # True, se puede hacer el giro
    print(cuenta.saldo)  # 500, saldo actualizado después del giro
    print(cuenta.girar(800))  # False, no se puede hacer el giro
    print(cuenta.saldo)  # 500, saldo no se actualiza porque el giro no se realizó
