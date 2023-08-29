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
            kilometros_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_faltantes
            self.cuenta_kilometros += distancia - kilometros_faltantes
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            max_litros_permitidos = self.capacidad_estanque - self.nivel_estanque
            return max_litros_permitidos, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_total = 500  # Kilómetros

    veces_cargar_combustible = 0
    while distancia_total > 0:
        autonomia_actual = auto.autonomia()
        if autonomia_actual >= distancia_total:
            distancia_total = 0
        else:
            distancia_total -= autonomia_actual
            litros_cargar = distancia_total / auto.rendimiento
            litros_cargar, exito = auto.llenar_estanque(litros_cargar)
            if not exito:
                distancia_total = 0
            veces_cargar_combustible += 1

    print("Cantidad de veces que tendrás que detenerte a cargar combustible:", veces_cargar_combustible)
