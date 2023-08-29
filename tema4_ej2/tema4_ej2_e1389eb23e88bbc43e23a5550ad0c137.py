class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        
    def reiniciar_cuentakilometros(self):
        self.kilometraje=0
        
    def andar(self, velocidad, tiempo):
        viaje_km=10000
        distancia_rec=velocidad*tiempo
        litros_gastados=distancia_rec/self.rendimiento
        self.nivel_estanque=self.nivel_estanque-litros_gastados
        self.kilometraje+=velocidad*tiempo
        self.cuenta_kilometros= self.cuenta_kilometros+distancia_rec
        if self.cuenta_kilometros >=viaje_km:
            return 0
        else:
            return (viaje_km-self.cuenta_kilometros)
        
    def autonomia(self):
        kilometros=self.rendimiento*self.nivel_estanque
        return kilometros
    
    def llenar_estanque(self,litros):
        a= self.nivel_estanque+litros
        if a > self.capacidad_estanque:
            t=(self.capacidad_estanque-self.nivel_estanque, False)
            return (t)
        else:
            self.nivel_estanque=a
            t= (a,True)
            return (t)

if __name__ == "__main__":
    auto=Auto(100,12)

         