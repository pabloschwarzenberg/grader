class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def __lt__(self,other):
        if self.nivel_estanque < other:
            return True
        else:
            return False

    def __add__(self, other):
        return self.nivel_estanque + other

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo_de_viaje):
        distancia_recorrida = velocidad * tiempo_de_viaje
        self.kilometraje = self.cuenta_kilometros + distancia_recorrida
        self.cuenta_kilometros = self.cuenta_kilometros + distancia_recorrida
        litros_utilizados = (distancia_recorrida / self.rendimiento)
        self.nivel_estanque = self.nivel_estanque - litros_utilizados
        if self.nivel_estanque < 0:
            return 0
        else:
            return 0 - self.nivel_estanque

    def autonomia(self):
        kilometros_restantes = self.rendimiento * self.nivel_estanque
        return kilometros_restantes

    def llenar_estanque(self, litros):
        if self.nivel_estanque + litros > self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        else:
            self.nivel_estanque = self.nivel_estanque + litros
            return (self.nivel_estanque, True)

if __name__ == "__main__":
    auto=Auto(100,12)
         