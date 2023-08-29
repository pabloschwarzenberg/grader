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
cuenta = CuentaCorriente("12345678-9", 5000)

puede_girar = cuenta.girar(2000)
print(puede_girar)  # Imprime True
print(cuenta.saldo)  # Imprime 3000

puede_girar = cuenta.girar(4000)
print(puede_girar)  # Imprime False
print(cuenta.saldo)  # Imprime 3000
         