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
            faltante = litros_necesarios - self.nivel_estanque
            self.kilometraje += self.nivel_estanque * self.rendimiento
            self.cuenta_kilometros += self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            return faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque:
            self.nivel_estanque = litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


# Ejemplo de uso
if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_viaje = 500  # Distancia total del viaje en kilómetros
    velocidad_viaje = 80  # Velocidad promedio durante el viaje en km/h
    tiempo_viaje = distancia_viaje / velocidad_viaje  # Tiempo de viaje en horas

    veces_detencion = 0

    while distancia_viaje > 0:
        faltante = auto.andar(velocidad_viaje, tiempo_viaje)
        if faltante > 0:
            veces_detencion += 1
            litros_a_cargar, exito = auto.llenar_estanque(faltante)
            distancia_viaje -= litros_a_cargar * auto.rendimiento
        else:
            distancia_viaje -= auto.nivel_estanque * auto.rendimiento
            auto.llenar_estanque(auto.capacidad_estanque)

    print("Número de veces de detención para cargar combustible:", veces_detencion)

