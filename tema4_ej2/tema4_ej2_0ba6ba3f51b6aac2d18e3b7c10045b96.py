class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometro=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometro(self):
        self.cuenta_kilometro=0
        return self.cuenta_kilometro
    def andar(self,velocidad,tiempo):
        self.nivel_estanque=self.nivel_estanque-(velocidad*tiempo)/self.rendimiento
        self.kilometraje=self.kilometraje+(velocidad*tiempo)
        self.cuenta_kilometro=self.cuenta_kilometro+(velocidad*tiempo)
        if self.nivel_estanque>=0:
            return str(0)
        elif self.nivel_estanque<0:
            return str(self.cuenta_kilometro)
        return self.nivel_estanque
    def autonomia(self):
        recorrido=self.nivel_estanque*self.rendimiento
        return recorrido
    def llenar_estanque(self,cantidad_litros):
        if (self.nivel_estanque+cantidad_litros)<100:
            self.nivel_estanque=self.nivel_estanque+cantidad_litros
            return self.nivel_estanque,True
        else:
            return self.capacidad_estanque,False
        pass

if __name__ == "__main__":
    auto=Auto(100,12)
         