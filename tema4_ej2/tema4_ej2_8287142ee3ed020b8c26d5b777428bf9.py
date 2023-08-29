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
            self.kilometraje += distancia_recorrida - distancia_faltante
            self.cuenta_kilometros += distancia_recorrida - distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

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
    distancia_viaje = 500
    velocidad = 80
    tiempo_viaje = distancia_viaje / velocidad

    paradas_carga = 0
    distancia_restante = distancia_viaje
    while distancia_restante > 0:
        if auto.nivel_estanque <= 0:
            max_litros, exito = auto.llenar_estanque(auto.capacidad_estanque)
            if not exito:
                break
            paradas_carga += 1

        distancia_faltante = auto.andar(velocidad, tiempo_viaje)
        if distancia_faltante > 0:
            distancia_restante = distancia_faltante
        else:
            distancia_restante = 0

    print("Cantidad de paradas de carga:", paradas_carga)
         