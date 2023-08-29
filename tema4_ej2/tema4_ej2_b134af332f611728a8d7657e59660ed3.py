class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_km = 0
        self.capacidad = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakm(self):
        self.cuenta_km = 0

    def andar(self,v,t):
        d = v*t
        self.kilometraje += d
        self.cuenta_km += d
        self.nivel_estanque -= self.rendimiento / d
        if self.nivel_estanque == 0:
            return 0
        else:
            return d - (self.rendimiento / d)

    def autonomia(self):
        return self.capacidad / self.rendimiento

    def llenar_estanque(self,l):
        if self.nivel_estanque + l > 100:
            return l - (100-self.nivel_estanque + l), False
        else:
            return self.nivel_estanque + l, True
        

if __name__ == "__main__":
    auto=Auto(100,12)
         