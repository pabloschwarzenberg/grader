class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo_de_viaje):
        self.nivel_estanque-=(velocidad*tiempo_de_viaje)/self.rendimiento
        self.kilometraje=velocidad*tiempo_de_viaje
        self.cuenta_kilometros=velocidad*tiempo_de_viaje
        if self.nivel_estanque>=0:
            return 0
        else:
            return self.nivel_estanque*(-1)*self.rendimiento

    def autonomia(self):
        return (self.nivel_estanque*self.rendimiento)

    def llenar_estanque(self,litros):
        if litros<=self.capacidad_estanque-self.nivel_estanque:
            self.nivel_estanque+=litros
            return (self.nivel_estanque,True)
        else:
            return (self.capacidad_estanque-self.nivel_estanque,False)