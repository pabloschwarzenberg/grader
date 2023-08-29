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
            kilometros_restantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_restantes
            self.cuenta_kilometros += distancia - kilometros_restantes
            self.nivel_estanque = 0
            return kilometros_restantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        litros_permitidos = self.capacidad_estanque - self.nivel_estanque
        if litros <= litros_permitidos:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            return litros_permitidos, False

if __name__ == "__main__":
    auto = Auto(100, 12)

    # Ejemplo de uso
    litros_iniciales = 60
    velocidad = 120
    tiempo = 1

    auto.llenar_estanque(litros_iniciales)
    print("Autonomía inicial:", auto.autonomia())

    distancia_recorrida = velocidad * tiempo
    auto.andar(velocidad, tiempo)
    print("Estanque después de viajar 1 hr:", auto.nivel_estanque, "litros")

    litros_restantes, exito = auto.llenar_estanque(50)
    print("Litros permitidos para llenar el estanque:", litros_restantes)
    print("Resultado del llenado del estanque:", exito)
