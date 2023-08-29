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

    def depositar(self, monto):
        self.saldo += monto

    def obtener_saldo(self):
        return self.saldo

    def obtener_rut(self):
        return self.rut


if __name__ == "__main__":
    cuenta = Cuenta("12345678-9", 10000)
    print(cuenta.obtener_rut()) 
    print(cuenta.obtener_saldo()) 
    cuenta.girar(5000)
    print(cuenta.obtener_saldo()) 
    cuenta.depositar(2000)
    print(cuenta.obtener_saldo()) 

           