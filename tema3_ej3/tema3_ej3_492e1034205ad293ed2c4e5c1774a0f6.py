class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto > self.saldo:
            return False

        self.saldo -= monto
        return True

# Crear una instancia de la clase Cuenta
cuenta_1 = Cuenta("12864303-6", 10000)