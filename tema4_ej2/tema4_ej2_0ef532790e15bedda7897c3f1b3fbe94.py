class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque  
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuentakilometro=0
    def andar(self,velocidad,tiempo):
        self.kilometraje=self.velocidad*self.tiempo
        self.cuentakilometros=self.velocidad*self.tiempo
        if self.cuentakilometros/self.rendimiento<=capacidad_estanque:
            return True
        elif self.cuentakilometros/self.rendimiento>self.capacidad_estanque:  
            red=(self.rendimiento*(self.capacidad_estanque-self.cuentakilometros/self.rendimiento
            return red
  
    def autonomia(self): 
        return(self.rendimiento(self.capacidad_estanque-self.cuentakilometros/self.rendimiento))
        
        
            


         