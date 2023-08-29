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
    cuenta = Cuenta("123456789", 5000)
    print(cuenta.saldo)  # Salida: 5000
    print(cuenta.girar(2000))  # Salida: True
    print(cuenta.saldo)  # Salida: 3000
    print(cuenta.girar(4000))  # Salida: False
    print(cuenta.saldo)  # Salida: 3000           