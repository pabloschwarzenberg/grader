class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometro = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometro = 0
        return self

    def andar(self, velocidad, tiempo_de_viaje):
        kilometros  = velocidad * tiempo_de_viaje
        kilometros_posibles = self.nivel_estanque * self.rendimiento
        
        if kilometros_posibles >= kilometros:
            self.nivel_estanque = (kilometros_posibles - kilometros)/self.rendimiento
            self.cuenta_kilometros = kilometros_posibles
            self.kilometraje += kilometros_posibles
            return 0

        else:
            falta = kilometros - kilometros_posibles
            self.cuenta_kilometros = kilometros
            self.kilometraje += kilometros
            return falta
        
    def autonomia(self):
        recorrer = self.rendimiento * self.nivel_estanque
        return recorrer

    def llenar_estanque(self, litros):
        actual = self.nivel_estanque + litros
        if actual > self.capacidad_estanque:
            maximo = self.capacidad_estanque - self.nivel_estanque
            return maximo, False
        else:
            self.nivel_estanque = actual
            return actual, True


if __name__ == "__main__":
    auto = Auto(100, 12)