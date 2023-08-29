class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,giro):
        if self.saldo < giro:
            print("Su giro excedio su propio Saldo")
            return False
        else:
            self.saldo = self.saldo - giro
            print("Realizo su giro exitosamente, quedo con un saldo final de", self.saldo)
            return True
if __name__ == "__main__":
    saldo = int(input("Saldo?: "))
    z = Cuenta("19129838-1", saldo)
    plata = int(input("Giro?:"))
    z.girar(plata)

