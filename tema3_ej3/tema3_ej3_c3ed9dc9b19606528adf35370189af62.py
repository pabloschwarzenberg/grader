class Cuenta:
    def __init__(self,rut,saldo):
        self.saldo=saldo
    def girar(self,monto):
        if monto>self.saldo:
          return False  
        else:  
          self.saldo=(int(self.saldo)-(int(monto)))
          return True