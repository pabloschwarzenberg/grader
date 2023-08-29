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
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False

if __name__ == "__main__":
    auto = Auto(100, 12)

    velocidad = 80
    tiempo = 2
    faltante = auto.andar(velocidad, tiempo)
    print("Kilómetros recorridos:", auto.kilometraje)
    print("Cuenta kilómetros:", auto.cuenta_kilometros)
    print("Faltaron por recorrer:", faltante, "litros")

    print("Autonomía:", auto.autonomia())

    litros = 60
    llenado = auto.llenar_estanque(litros)
    print("Litros en el estanque:", llenado[0])
    print("Éxito al llenar el estanque:", llenado[1])

         