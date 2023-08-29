class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        self.kilometraje += velocidad*tiempo
        self.cuenta_kilometros += velocidad*tiempo
        distancia_max = self.rendimiento*self.nivel_estanque
        if distancia_max >= (velocidad*tiempo):
            self.nivel_estanque=self.nivel_estanque-(velocidad*tiempo)/self.rendimiento
            return 0
        else:
            return (velocidad*tiempo)-distancia_max
    def autonomia(self):
        return (self.rendimiento*self.nivel_estanque)
    def llenar_estanque(self,litros):
        if litros+self.nivel_estanque>self.capacidad_estanque:
            return [self.capacidad_estanque-self.nivel_estanque,False]
        else:
            self.nivel_estanque+=litros
            return [self.nivel_estanque,True]



if __name__ == "__main__":
    auto=Auto(100,12)         