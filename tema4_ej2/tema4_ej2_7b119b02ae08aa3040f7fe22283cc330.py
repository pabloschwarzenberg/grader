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
        combustible_necesario = distancia / self.rendimiento

        if combustible_necesario <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= combustible_necesario
            return 0
        else:
            km_faltantes = (combustible_necesario - self.nivel_estanque) * self.rendimiento
            self.kilometraje += self.nivel_estanque * self.rendimiento
            self.cuenta_kilometros += self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            return km_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        litros_maximos = self.capacidad_estanque - self.nivel_estanque
        if litros <= litros_maximos:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            return litros_maximos, False


if __name__ == "__main__":
    auto = Auto(100, 12)  # Estanque de 100 litros y rendimiento de 12 km/l

    distancia_total = 500  # Distancia total del viaje en kilómetros
    velocidad = 80  # Velocidad promedio en km/h

    tiempo_viaje = distancia_total / velocidad
    km_recorridos = 0
    veces_recarga = 0

    while km_recorridos < distancia_total:
        faltantes = auto.andar(velocidad, tiempo_viaje)
        km_recorridos += tiempo_viaje * velocidad

        if faltantes > 0:
            veces_recarga += 1
            litros_recarga, exito = auto.llenar_estanque(faltantes)
            if not exito:
                break

    print("Número de veces de recarga: ", veces_recarga)

         