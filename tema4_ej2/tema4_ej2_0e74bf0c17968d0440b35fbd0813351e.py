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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia_recorrida
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return distancia_faltante

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
    distancia_viaje = 500
    detenciones = 0

    while distancia_viaje > 0:
        autonomia = auto.autonomia()
        if distancia_viaje <= autonomia:
            distancia_viaje = 0
        else:
            distancia_viaje -= autonomia
            litros_necesarios = distancia_viaje / auto.rendimiento
            litros_restantes, exito = auto.llenar_estanque(litros_necesarios)
            if exito:
                distancia_viaje = 0
            else:
                distancia_viaje -= litros_restantes * auto.rendimiento
            detenciones += 1

    print("tienes detenerte a cargar combustible", detenciones, "veces.")

