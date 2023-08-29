class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, cantidad):
        if cantidad > self.saldo:
            return False
        else:
            self.saldo -= cantidad
            return True

if __name__ == "__main__":
    # Ejemplo de uso
    cuenta = Cuenta(123456789, 1000)
    print(cuenta)
    print(cuenta.girar(500))
    print(cuenta)
    