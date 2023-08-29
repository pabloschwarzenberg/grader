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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - self.cuenta_kilometros
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia - distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_total = 1000
    velocidad = 80
    tiempo_viaje = distancia_total / velocidad

    veces_carga = 0
    while distancia_total > 0:
        falta_combustible = auto.andar(velocidad, tiempo_viaje)
        if falta_combustible > 0:
            veces_carga += 1
            litros_a_cargar, _ = auto.llenar_estanque(falta_combustible)
            distancia_total -= litros_a_cargar * auto.rendimiento
        else:
            distancia_total -= distancia_total

    print("Tendrás que detenerte a cargar combustible {} veces en el viaje.".format(veces_carga))
