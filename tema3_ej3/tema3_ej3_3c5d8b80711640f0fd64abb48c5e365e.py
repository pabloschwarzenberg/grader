class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,monto):
        if monto<=self.saldo:
            self.saldo-=monto
            return True
        else:
            return False
    
if __name__ == "__main__":
    cuenta=Cuenta("12345678-9",100000)
    print(cuenta.girar(50000))
    print(cuenta.saldo)
    print(cuenta.girar(80000))
    print(cuenta.saldo)

           