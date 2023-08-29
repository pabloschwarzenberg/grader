class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def andar(self,velocidad,tiempo):
        self.kilometraje+=velocidad*tiempo
        self.cuenta_kilometros+=velocidad*tiempo
        self.nivel_estanque=self.capacidad_estanque-(self.rendimiento*velocidad*tiempo) 
if __name__ == "__main__":
    auto=Auto(100,12)
         