class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.nivel_estanque = 0
        self.cuenta_kilometros=  0    
        
    def llenar_estanque(self,cantidad_litros):
        if (self.nivel_estanque)+(cantidad_litros) > self.capacidad_estanque:
            litros_max=((self.capacidad_estanque)-(self.nivel_estanque))
            return (litros_max,False)
        else:
            self.nivel_estanque = (self.nivel_estanque)+(cantidad_litros)
            return (self.nivel_estanque,True) 
    
    def autonomia(self):
        
        return ((self.nivel_estanque)*(self.rendimiento))

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
        return self.cuenta_kilometros
            
    def andar(self,velocidad,tiempo_viaje):
        if self.autonomia() > (velocidad)* (tiempo_viaje) :
            self.cuenta_kilometros=(velocidad)*(tiempo_viaje)
            self.kilometraje += (velocidad)* (tiempo_viaje)
            self.nivel_estanque = self.nivel_estanque-((velocidad)* (tiempo_viaje)//(self.rendimiento))
            return 0
        else:
            return (velocidad)* (tiempo_viaje) - self.autonomia()
          
    
            
    