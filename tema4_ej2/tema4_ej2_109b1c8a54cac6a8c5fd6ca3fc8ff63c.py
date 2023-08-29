class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempodeviaje):
        distancia=velocidad*tiempodeviaje
        distanciacapaz=self.rendimiento*self.nivel_estanque
        if distancia>distanciacapaz:
            return distancia-distanciacapaz
        else:
            self.kilometraje+=distancia
            self.cuenta_kilometros+=distancia
            self.nivel_estanque=self.nivel_estanque-(distancia/self.rendimiento)
            return 0

    def autonomia(self):
        return self.rendimiento*self.nivel_estanque

    def llenar_estanque(self,litros):
        if litros>(self.capacidad_estanque-self.nivel_estanque):
            return self.capacidad_estanque-self.nivel_estanque,False
        else:
            self.nivel_estanque+=litros
            return self.nivel_estanque,True


auto=Auto(60,12)
auto.llenar_estanque(60)
         