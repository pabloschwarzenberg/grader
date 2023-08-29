class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        pass

if __name__ == "__main__":
    auto=Auto(100,12)
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
            kilometros_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += (distancia - kilometros_faltantes)
            self.cuenta_kilometros += (distancia - kilometros_faltantes)
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= (self.capacidad_estanque - self.nivel_estanque):
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    viaje = [(120, 2), (80, 1), (100, 3)]  # Ejemplo de velocidades y tiempos de viaje

    paradas_carga = 0
    for velocidad, tiempo in viaje:
        resultado = auto.andar(velocidad, tiempo)
        if resultado > 0:
            paradas_carga += 1

    print("Paradas necesarias para cargar combustible:", paradas_carga)

         