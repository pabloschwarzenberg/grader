# completa el código de la función
class Cuenta:
      def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
        
      def girar(self,giro):
          if self.saldo<giro:
            return False
          if self.saldo>=giro:
            self.saldo=(self.saldo)-giro
            return True
      def __str__(self):

          return "{0},{1}".format(self.rut,self.saldo)


           