class Auto:
    kilometraje=float
    cuenta_kilometros=float
    nivel_estanque=float

    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
    
    def llenar_estanque(self, carga):
        llenado=self.nivel_estanque+carga
        if llenado<=self.capacidad_estanque:
            self.nivel_estanque=llenado
            return self.nivel_estanque, True
        else:
            return llenado-self.capacidad_estanque, False

    def autonomia(self):
        km=self.nivel_estanque*self.rendimiento
        return km

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        consumo=distancia/self.rendimiento
        if (self.nivel_estanque-consumo)>=0:
            self.kilometraje=self.kilometraje+distancia
            self.cuenta_kilometros=self.cuenta_kilometros+distancia
            self.nivel_estanque=self.nivel_estanque-consumo
            return 0
        else:
            return distancia - (self.nivel_estanque*self.rendimiento)
if __name__ == "__main__":
    auto=Auto(100,12)
         