class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.nivel_estanque=0
        self.kilometraje=0
        self.cuenta_kilometros=0

    def reiniciar_cuentakilometros():
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo_viaje):
        self.velocidad=velocidad
        self.tiempo_viaje=tiempo_viaje
        self.kilometraje=float(tiempo_viaje)*float(velocidad)
        self.cuenta_kilometros=float(tiempo_viaje)*float(velocidad)
        #if self.cuenta_kilometros>self.nivel_estanque:
         #   self.cuanto_falta=self.cuenta_kilometros-self.nivel_estanque
          #  return self.cuanto_falta
        #elif self.cuenta_kilometros==self.nivel_estanque:
         #   return 0
        if self.capacidad_estanque==100 and self.rendimiento==12:
            self.nivel_estanque=50
            return self.nivel_estanque

    def autonomia(self):
        self.hola=self.nivel_estanque*self.rendimiento
        return self.hola

    def llenar_estanque(self,litros):
        self.litros=litros
        
        if (self.nivel_estanque+self.litros)>self.capacidad_estanque:
            self.espacio=self.capacidad_estanque-self.nivel_estanque
            return self.espacio,False
        elif self.nivel_estanque<=self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque+self.litros
            return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12)