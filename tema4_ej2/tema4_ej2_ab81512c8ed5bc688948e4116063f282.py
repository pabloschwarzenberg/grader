class Auto:
     def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento =rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
        
     def reiniciar_cuentakilometros(self):
       self.cuenta_kilometros = 0
     
     def andar(self,velocidad,tiempo):
       nivel = self.nivel_estanque - ((velocidad*tiempo)/self.rendimiento)
       self.kilometraje += (velocidad*tiempo)
       self.cuenta_kilometros += (velocidad*tiempo)
       if nivel<0:
         return 0-nivel
       elif nivel >= 0 :
         self.nivel_estanque = nivel
         return 0
     
     def autonomia(self):
       kilometros = (self.nivel_estanque*self.rendimiento)
       return kilometros
     
     def llenar_estanque(self,litros):
       
       if litros<self.capacidad_estanque-self.nivel_estanque:
         self.nivel_estanque += litros 
         return (self.capacidad_estanque-self.nivel_estanque,False)
       else:
         return (self.capacidad_estanque-self.nivel_estanque,True)
       

if __name__ == "__main__":
    auto=Auto(100,12)
         