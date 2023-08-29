# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut=rut
        self.saldo=saldo
    def girar (self,giro):
        if self.saldo>=giro:
            nuevosaldo=self.saldo-giro
            print ("Había un saldo inicial de",self.saldo, ", al girar", giro,"quedan",nuevosaldo)
            self.saldo=nuevosaldo
            return True

        elif self.saldo<giro:
            pass
            return False
          