class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = 100
        self.nivel_estanque = 0
        self.rendimiento = 12

    def reiniciar_cuentakilometros(self):
        if self.cuenta_kilometros != 0:
            self.cuenta_kilometros = 0
        return self.cuenta_kilometros

    def autonomia (self):
        km = self.nivel_estanque*12
        return km

    def andar (self, velocidad, tiempo_viaje):
        self.distancia = velocidad/tiempo_viaje
        if self.distancia/12 > self.nivel_estanque:
            faltan = (self.distancia/12 - self.nivel_estanque)*12
            self.nivel_estanque = 0
        else:
            faltan = 0
            self.nivel_estanque = self.capacidad_estanque - (self.distancia * 12)
        self.cuenta_kilometros += self.distancia
        self.nivel_estanque = self.capacidad_estanque - (self.distancia * 12)
        return faltan



    def llenar_estanque (self, litros):
        self.litros = litros
        maximo = 100 - self.nivel_estanque
        if litros > maximo:
            return [100, False]
        else:
            self.nivel_estanque += litros
            return [self.nivel_estanque, True]

if __name__ == "__main__":
    auto = Auto(100, 12)
