class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuanta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuanta_kilometros = 0

    def andar(self, velocidad, tiempo):
        km = velocidad * tiempo
        vencina = km / self.rendimiento

        if self.nivel_estanque > vencina:
            self.nivel_estanque -= vencina
            self.kilometraje += km
            self.cuanta_kilometros += km
            return 0

        else:
            km -= self.nivel_estanque * self.rendimiento
            return km

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if self.capacidad_estanque < self.nivel_estanque + litros:
            return self.capacidad_estanque, False

        self.nivel_estanque += litros
        return self.nivel_estanque, True
        

if __name__ == "__main__":
    auto=Auto(100,12)