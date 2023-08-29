# completa el código de la función

class Cuenta:
    def __init__(self,rut,saldo,giro):
      self.rut=input("ingrese rut: ")
      self.saldo=input("ingrese su saldo: ")
      self.giro=input(" cuanto desea sacar: ")
    def girar(self):
      r=float(self.rut)
      s=float(self.saldo)
      g=float(self.giro)
      if g>s:
        print(False)
      elif g<=s:
        print(True)
        s=s-g
        print(s)
    def __str__(self): 
      return(str(girar))
      
if __name__=="__main__":      
  p=Cuenta("rut","saldo","giro")
  p.girar()




    
    
           