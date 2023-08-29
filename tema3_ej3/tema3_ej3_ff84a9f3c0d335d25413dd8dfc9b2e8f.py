class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def __str__(self):
        return "Cuenta: {0}, Saldo: {1}".format(self.rut,self.saldo)

    def girar(self,giro):
        if self.saldo>=giro:
          self.saldo=self.saldo-giro
          return True
        else:
          return False

#if __name__ == "__main__":
#    rut="19954251-6"
#    saldo=int(input("Ingrese saldo: "))
#    c1=Cuenta(rut,saldo)
#    print(c1.girar(c1.saldo))
#    print(c1.saldo)