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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia
            self.kilometraje += (velocidad - (distancia_faltante / tiempo)) * tiempo
            self.cuenta_kilometros += (velocidad - (distancia_faltante / tiempo)) * tiempo
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    velocidad_viaje = 80
    tiempo_viaje = 5
    distancia_viaje = velocidad_viaje * tiempo_viaje

    veces_carga = 0

    while distancia_viaje > 0:
        resultado_andar = auto.andar(velocidad_viaje, tiempo_viaje)
        if resultado_andar == 0:
            veces_carga += 1
        else:
            veces_carga += 1
            auto.llenar_estanque(auto.capacidad_estanque)

        distancia_viaje -= auto.cuenta_kilometros

    print("TendrÃ¡s que detenerte a cargar combustible", veces_carga, "veces en el viaje.")