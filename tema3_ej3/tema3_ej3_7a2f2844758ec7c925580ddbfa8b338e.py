# completa el código de la función
class Cuenta:
  def __init__(self,Rut,Saldo):
      self.__Rut=Rut
      self.__Saldo=Saldo
  def girar(self,Saldo):
      return self.__Saldo
  def setgirar(self,s):
     if(self.Saldo - s > 0):
       self.__Saldo=self.Saldo - s
  def getRut(self):
     return self.__Rut
  def getSaldo(self):
     return self.__Saldo
  def MostrarCuenta(self):
     print(“Cuenta Corriente, Rut:” + self.getRut() + “Saldo:” + str(self.getSaldo())
Rut=raw_input(“Ingresar Rut:”)
Saldo=input(“Ingresa Saldo Inicial:”)
M=Cuenta(Rut,Saldo)
M.MostrarCuenta()
      
           