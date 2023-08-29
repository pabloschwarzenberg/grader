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
        distancia=velocidad*tiempo
        self.nivel_estanque=(self.nivel_estanque)-(distancia/self.rendimiento)
        self.kilometraje+=distancia
        self.cuenta_kilometros+=distancia
        if self.nivel_estanque<=0:
            return self.nivel_estanque
        else:
            return 0
    def autonomia(self):
        a=self.nivel_estanque*self.rendimiento
        return a
    def llenar_estanque(self,litros):
        self.nivel_estanque=litros
        if (self.nivel_estanque+litros)>self.capacidad_estanque:
            maxima=self.capacidad_estanque-self.nivel_estanque
            return {maxima,False}
        else:
            return {self.nivel_estanque,True}

        pass


if __name__ == "__main__":
    auto = Auto(100, 12)
