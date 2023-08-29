class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometro(self):
        self.cuenta_kilometros=0
        
    
    def andar (self,velocidad,tiempo):
        distancia=velocidad*tiempo
        capacidad=self.nivel_estanque*self.rendimiento
        if distancia<=capacidad:
            perdidos=distancia/self.rendimiento
            self.kilometraje=self.kilometraje+distancia
            self.cuenta_kilometros=self.cuenta_kilometros+distancia
            self.nivel_estanque=self.nivel_estanque-perdidos
            return 0
        else:
          self.kilometraje=self.kilometraje+capacidad
          self.cuenta_kilometros=self.cuenta_kilometros+capacidad
          diferencia=distancia-capacidad
          self.nivel_estanque=0
          return diferencia
    
    def autonomia (self):
       puederecorrer=self.rendimiento*self.nivel_estanque
       return puederecorrer
    
    def llenar_estanque(self,litros):
       self.nivel_estanque=litros
       if self.nivel_estanque<=self.capacidad_estanque:
         return (self.nivel_estanque,True)
       else:
         if self.capacidad_estanque<self.nivel_estanque :
             return(self.capacidad_estanque,False)
            
if __name__ == "__main__":
    auto=Auto(100,12)


         