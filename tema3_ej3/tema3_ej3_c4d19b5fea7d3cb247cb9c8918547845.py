# completa el código de la función

class Cuenta:

    def __init__(self,rut,saldo):

        self.rut = rut
        self.saldo = saldo

    def girar(self,giro):

        if giro < self.saldo:

            self.saldo = self.saldo-giro
            print(self.saldo)
            return True


        else:
            return False
           