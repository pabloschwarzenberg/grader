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
            kilometros_faltantes = litros_necesarios * self.rendimiento
            self.kilometraje += kilometros_faltantes
            self.cuenta_kilometros += kilometros_faltantes
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    velocidad = float(input("Ingrese la velocidad del viaje (km/h): "))
    tiempo = float(input("Ingrese el tiempo de viaje (horas): "))

    veces_carga = 0

    while True:
        autonomia_actual = auto.autonomia()

        if autonomia_actual >= velocidad * tiempo:
            break

        litros_carga = auto.capacidad_estanque - auto.nivel_estanque
        veces_carga += 1
        auto.llenar_estanque(litros_carga)

    print("Tendrás que detenerte a cargar combustible", veces_carga, "veces durante el viaje.")   