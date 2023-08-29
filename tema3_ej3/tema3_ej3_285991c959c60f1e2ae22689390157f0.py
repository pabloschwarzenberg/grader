# completa el código de la función
# completa el código de la clase
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,monto):
        if self.saldo >= monto:
            saldo_final=(self.saldo)-(monto)
            self.saldo=saldo_final
            return True
            
        else:
            return False
        
           