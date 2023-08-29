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
        distancia_recorrida = velocidad * tiempo
        litros_consumidos = distancia_recorrida / self.rendimiento

        if litros_consumidos <= self.nivel_estanque:
            self.nivel_estanque -= litros_consumidos
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            return 0
        else:
            distancia_faltante = (litros_consumidos - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > self.capacidad_estanque - self.nivel_estanque:
            max_litros_permitidos = self.capacidad_estanque - self.nivel_estanque
            return max_litros_permitidos, False
        else:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True


if __name__ == "__main__":
    auto = Auto(100, 12)
    viaje = [(80, 2), (70, 3), (60, 4), (90, 1)]

    detenciones = 0

    for velocidad, tiempo in viaje:
        distancia_faltante = auto.andar(velocidad, tiempo)
        if distancia_faltante > 0:
            detenciones += 1
            litros_necesarios = distancia_faltante / auto.rendimiento
            litros_permitidos, exito = auto.llenar_estanque(litros_necesarios)
            if exito:
                auto.andar(velocidad, tiempo)
                detenciones -= 1

    print("Número de detenciones necesarias:", detenciones)