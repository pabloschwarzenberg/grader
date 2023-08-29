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
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            distancia_restante = self.rendimiento * self.nivel_estanque
            self.kilometraje += distancia_restante
            self.cuenta_kilometros += distancia_restante
            self.nivel_estanque = 0
            return distancia - distancia_restante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque:
            litros = self.capacidad_estanque
        self.nivel_estanque = litros

    def __str__(self):
        return "Estanque: {self.nivel_estanque} l, Rendimiento: {self.rendimiento} km/l"


if __name__ == "__main__":
    auto = Auto(100, 12)

    # Ejemplo de uso
    print("Autonomía:", auto.autonomia())

    auto.llenar_estanque(60)
    print(auto)

    auto.andar(120, 1)
    print(auto)


         