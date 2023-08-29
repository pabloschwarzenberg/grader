class Auto:
    def __init__(self,capacidad_estanque, rendimiento):
        self.capacidad_estanque= capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0 
        self.nivel_estanque = 0
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
   
    def andar(self,velocidad,tiempodeviaje):
        self.kilometraje += velocidad*tiempodeviaje
        self.cuenta_kilometros += velocidad*tiempodeviaje
        self.nivel_estanque -= (velocidad*tiempodeviaje)/self.rendimiento
        if self.nivel_estanque >=0:
          return 0
        else:
          return (velocidad*tiempodeviaje)%self.rendimiento
    
    def autonomia(self):
        autonomia = self.nivel_estanque*self.rendimiento
        return autonomia
        
    def llenar_estanque(self,cantidadlitros):
         if self.nivel_estanque + cantidadlitros > self.capacidad_estanque:
             return(self.capacidad_estanque-self.nivel_estanque,False)
         else:
             self.nivel_estanque += cantidadlitros
             return(self.nivel_estanque,True)

         