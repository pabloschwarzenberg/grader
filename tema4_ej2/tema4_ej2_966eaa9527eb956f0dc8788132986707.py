class Auto:

    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,v,t):
        d = v * t
        consumo = d / self.rendimiento
        if consumo <= self.nivel_estanque:
            self.cuenta_kilometros += d
            self.kilometraje += d
            self.nivel_estanque -= consumo
            return 0
        else:
            drec = self.rendimiento * self.nivel_estanque
            self.cuenta_kilometros += drec
            self.kilometraje += drec
            self.nivel_estanque = 0
            return (d-drec)

    def autonomia(self):
        autonomia = self.nivel_estanque*self.rendimiento
        return autonomia

    def llenar_estanque(self,litros):
        if self.nivel_estanque + litros >  self.capacidad_estanque:
            return (self.capacidad_estanque,False)
        else:
            self.nivel_estanque += litros
            return (self.nivel_estanque,True)
if __name__ == "__main__":
    auto=Auto(100,12)
         