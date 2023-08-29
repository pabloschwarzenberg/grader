class Cuenta:
    def __init__(self,rut='1234-5',saldo=10000,monto_retirar=3000):
        self.rut=rut
        self.saldo=saldo
        self.monto=monto_retirar
    
    def girar(self,monto_retirar):
        self.monto=monto_retirar
        if int(self.monto)>int(self.saldo):
            return False
        else:
           return True
        
    def montoRestante(self):
        return int(self.saldo)-int(self.monto)
        
    def __repr__(self):
        return 'Dinero retirado: {0}\nDinero en cuenta: {1}'.format(self.monto,int(self.saldo)-int(self.monto))
  
  
           