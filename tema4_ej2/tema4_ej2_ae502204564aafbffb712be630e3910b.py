class Auto:
    def __init__(self, capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuentakilometros=0
        self.capacidadestanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuentakilometros=0
        return

    def andar(self, velocidad, tiempo):
        distancia=velocidad*tiempo
        if self.rendimiento*self.nivel_estanque>=distancia:
            self.nivel_estanque=self.nivel_estanque-distancia/self.rendimiento
            self.kilometraje+=distancia
            self.cuentakilometros+=distancia
            return 0
        else:
            self.nivel_estanque=0
            drecorrida=self.rendimiento*self.nivel_estanque
            faltante=distancia-drecorrida
            self.kilometraje+=drecorrida
            self.cuentakilometros+=drecorrida
            return "Faltaron",faltante,"kilómetros"

    def autonomia(self):
        kilometros=self.nivel_estanque*self.rendimiento
        return kilometros

    def llenar_estanque(self, litros):
        if self.nivel_estanque+litros>self.capacidadestanque:
            maximo=self.capacidadestanque-self.nivel_estanque
            return (False,maximo)
        else:
            self.nivel_estanque+=litros
            return (True,self.nivel_estanque)

if __name__ == "__main__":
    auto=Auto(100,12)
         