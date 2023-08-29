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
        self.kilometraje=velocidad*tiempo
        self.cuenta_kilometros=velocidad*tiempo
        self.nivel_estanque=capacidad_estanque-(velocidad*tiempo/rendimiento)
        if nivel_estanque==0:
            return distancia-self.cuenta_kilometros
        else:
            return 0
    def autonomia(self):
        return self.nivel_estanque*rendimiento
    def llenar_estanque(self,cantidad_de_litros):
        if self.capacidad_estanque<self.nivel_estanque+cantidad_de_litros:
            a=self.capacidad_estanque
            return (a,False)
        else:
            return (self.nivel_estanque+cantidad_de_litros,True)

if __name__ == "__main__":
    auto=Auto(100,12)
         