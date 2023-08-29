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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            litros_posibles = self.capacidad_estanque - self.nivel_estanque
            return litros_posibles, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    viaje = 500  
    tiempo_repostaje = 10  

    num_paradas = 0
    while viaje > 0:
        autonomia = auto.autonomia()
        if autonomia < viaje:
            distancia_recorrida = autonomia
            viaje -= autonomia
            tiempo_viaje = distancia_recorrida / 100 * 60  
            tiempo_repostaje += 10  
            auto.reiniciar_cuentakilometros()
            auto.llenar_estanque(auto.capacidad_estanque)
            num_paradas += 1
        else:
            distancia_recorrida = viaje
            tiempo_viaje = distancia_recorrida / 100 * 60  
            viaje = 0

        auto.andar(100, tiempo_viaje)

    print(f"Número de paradas para repostar combustible: {num_paradas}")
