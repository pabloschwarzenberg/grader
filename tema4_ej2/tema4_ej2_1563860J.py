class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo_de_viaje):
        self.velocidad=velocidad
        self.tiempo=tiempo_de_viaje
    def autonomia(self):
        autonomia=self.nivel_estanque*self.rendimiento
        return autonomia
    def llenar_estanque(self,bencina):
        self.bencina=bencina
        if self.nivel_estanque+self.bencina>self.capacidad_estanque:
            return self.capacidad_estanque,False
        else:    
            self.nivel_estanque+=self.bencina
            return self.nivel_estanque,True
if __name__ == "__main__":
    auto=Auto(100,12)
         