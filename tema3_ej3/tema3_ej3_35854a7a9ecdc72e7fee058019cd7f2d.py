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

# Ejemplo de uso
cuenta = Cuenta("123456789", 1000)
print(cuenta.girar(500))  # True, se puede girar 500
print(cuenta.saldo)  # 500, saldo actualizado
print(cuenta.girar(1000))  # False, no se puede girar 1000
print(cuenta.saldo)  # 500, saldo no se modificó
           