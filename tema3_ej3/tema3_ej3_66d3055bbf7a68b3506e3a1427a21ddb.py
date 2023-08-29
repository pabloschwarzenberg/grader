class Cuenta:
    rut=''
    saldo=''

    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=int(saldo)

    def girar(self):
        if girar<=self.saldo:
            nuevo_saldo=self.saldo-girar
            self.saldo=nuevo_saldo
            print(self.saldo)
            return True
        else:
            print("No puede retirar mas de lo que tiene en su cuenta " + str(self.saldo))
            return False
            
if __name__ == "__main__":
  cuenta=Cuenta("21.385.393-7","20000")            
  girar=int(input("Indique cuanto desea girar: "))
  print(cuenta.girar())