class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, vel, t):
        recorrido = vel * t
        litros = recorrido / self.rendimiento 
        if self.nivel_estanque - litros >= 0:
            self.nivel_estanque = self.nivel_estanque - litros
            return 0
        else:
            self.nivel_estanque = 0
            return abs(self.nivel - litros) * self.rendimiento
        self.kilometraje += recorrido
        self.cuenta_kilometros += recorrido 

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, bencina):
        if self.nivel_estanque + bencina <= self.capacidad_estanque:
            self.nivel_estanque += bencina
        else:
            return (self.capacidad_estanque, False)

if __name__ == "__main__":
    auto=Auto(100,12)