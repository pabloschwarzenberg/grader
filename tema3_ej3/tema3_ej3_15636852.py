# completa el código de la función
class Cuenta:
     def __init__(self,rut=123456,saldo=0):
          self.rut=rut
          self.saldo=saldo

     def girar(self,monto):
          y=monto<self.saldo
          
          if y==True:
               self.saldo-=monto
          return y
               
     def __str__(self):
          return "Su nuevo saldo es "+str(saldo)
     pass

if __name__ == "__main__":
  hh=Cuenta(123456,200000)
  hh.girar(2000)
  print(hh)