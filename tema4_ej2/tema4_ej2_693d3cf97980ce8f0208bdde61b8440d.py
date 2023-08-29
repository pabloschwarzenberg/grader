
class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        litros_necesarios = distancia / self.rendimiento
        if litros_necesarios <= self.nivel_estanque:
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            kilometros_restantes = (self.nivel_estanque * self.rendimiento)
            self.kilometraje += kilometros_restantes
            self.cuenta_kilometros += kilometros_restantes
            self.nivel_estanque = 0
            return distancia - kilometros_restantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    viaje = [(80, 2), (60, 3), (70, 2), (50, 4)]  # Lista de tuplas: (velocidad, tiempo)
    paradas = 0

    for velocidad, tiempo in viaje:
        faltante = auto.andar(velocidad, tiempo)
        if faltante > 0:
            paradas += 1

    print("Tendrás que detenerte a cargar combustible", paradas, "veces.")
