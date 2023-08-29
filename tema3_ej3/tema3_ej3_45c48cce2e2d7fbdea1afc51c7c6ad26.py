class Cuenta:
    def __init__(self,titular,monto):
        self.titular=titular
        self.saldo=monto

    def girar(self,monto):
        if self.saldo < monto:
            return False
        else:
            self.saldo=monto
            return True

if __name__ == "__main__":
    c=Cuenta("12864303-6",10000)
    c.girar(5000)
    print(c.saldo)
    c.saldo=10000
    print(c.girar(11000))