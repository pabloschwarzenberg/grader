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


if __name__ == "__main__":
    cuenta = Cuenta("21683316-3", 1000)
    print(cuenta.girar(500)) 
    print(cuenta.saldo)  
    print(cuenta.girar(1000))  
    print(cuenta.saldo)  
