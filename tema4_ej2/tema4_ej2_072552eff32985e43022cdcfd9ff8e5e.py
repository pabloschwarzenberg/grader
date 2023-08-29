class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self,cuenta_kilometros):
        self.cuenta_kilometros=0
        
    def andar(self,velocidad,tiempo_viaje):
        self.kilomelometraje+=velocidad*tiempo_viaje
        self.cuenta_kilometros+=velocidad*tiempo_viaje
        self.nivel_estanque-=velocidad*tiempo_viaje/self.rendimiento
        if self.nivel_estanque<0:
            falto=abs(nivel_estanque)*self.rendimiento
            return falto
        elif self.nivel_estanque>=0:
            return 0

    def autonomia(self,nivel_estanque,rendimiento):
        autonomias=self.rendimiento*self.nivel_estanque
        return autonomias

    def llenar_estanque(self,capacidad_estanque,nivel_estanque,litros):
        necesario=self.capacidad_estanque-self.nivel_estanque
        if necesario<litros:
            a=litros-necesario
            return a, False
        elif necesario>=litros:
            capacidad_estanque+=litros
            return capacidad_estanque, True


if __name__ == "__main__":
    auto=Auto(100,12)
         