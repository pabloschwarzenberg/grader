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
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            litros_maximos = self.capacidad_estanque - self.nivel_estanque
            return litros_maximos, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    viaje = [(100, 4), (80, 6), (60, 5), (90, 8)]

    paradas = 0
    for velocidad, tiempo in viaje:
        resultado = auto.andar(velocidad, tiempo)
        if resultado != 0:
            paradas += 1
            litros_faltantes = resultado / auto.rendimiento
            auto.llenar_estanque(litros_faltantes)

    print("Cantidad de paradas para cargar combustible:", paradas)

         