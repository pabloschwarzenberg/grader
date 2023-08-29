class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
            self.kilometraje = 0

    def andar(self, velocidad, tiempoviaje):
        kmtot = velocidad * tiempoviaje
        self.kilometraje = self.kilometraje + kmtot
        self.cuenta_kilometros = self.cuenta_kilometros + kmtot
        litrosUsados = kmtot / self.rendimiento
        self.nivel_estanque = self.nivel_estanque - litrosUsados
        if (self.nivel_estanque * self.rendimiento) >= kmtot:
            return 0
        else:
            kmrestantes = kmtot - (self.nivel_estanque * self.rendimiento)
            return kmrestantes

    def autonomia(self):
        kmPosibles = self.nivel_estanque * self.rendimiento 
        return kmPosibles

    def llenar_estanque(self, qlitros):
        litrosDisp = self.capacidad_estanque - self.nivel_estanque
        if litrosDisp > qlitros:
            self.nivel_estanque = self.nivel_estanque + qlitros
            tupi = (self.nivel_estanque, True)
        else:
            tupi = (litrosDisp, False)

if __name__ == "__main__":
    auto=Auto(100,12)
         