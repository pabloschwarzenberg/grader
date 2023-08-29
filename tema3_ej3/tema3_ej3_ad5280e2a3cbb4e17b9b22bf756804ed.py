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

# Ejemplo de uso
cuenta_1 = Cuenta("12864303-6", 10000)
print(cuenta_1.girar(5000))  # True
print(cuenta_1.saldo)  # 5000

print(cuenta_1.girar(8000))  # False
print(cuenta_1.saldo)  # 5000
