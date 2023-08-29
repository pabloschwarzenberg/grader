class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        recorrido=velocidad*tiempo
        gasto=recorrido/self.rendimiento
        if gasto<=self.nivel_estanque:
            self.nivel_estanque-=gasto
            self.kilometraje+=recorrido
            self.cuenta_kilometros+=recorrido
            return 0
        else:
            self.kilometraje +=self.nivel_estanque*self.rendimiento
            self.cuenta_kilometros+=self.nivel_estanque*self.rendimiento
            self.nivel_estanque=0
            return recorrido-self.nivel_estanque*self.rendimiento
    def autonomia(self):
        return self.rendimiento*self.nivel_estanque
    def llenar_estanque(self,cant):
        if self.nivel_estanque+cant>self.capacidad_estanque:
            return self.capacidad_estanque-self.nivel_estanque, False
        else:
            self.nivel_estanque+=cant
            return self.nivel_estanque, True


if __name__ == "__main__":
    auto=Auto(100,12)
         