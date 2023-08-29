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

# Ejemplo de uso
cuenta = Cuenta("12345678-9", 10000)
print(cuenta.saldo)  # Imprime: 10000
print(cuenta.girar(5000))  # Imprime: True
print(cuenta.saldo)  # Imprime: 5000
print(cuenta.girar(10000))  # Imprime: False
print(cuenta.saldo)  # Imprime: 5000

           