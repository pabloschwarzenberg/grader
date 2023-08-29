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

        if litros_necesarios > self.nivel_estanque:
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - distancia_faltante
            self.nivel_estanque = 0
            self.cuenta_kilometros += distancia - distancia_faltante
            return distancia_faltante
        else:
            self.kilometraje += distancia
            self.nivel_estanque -= litros_necesarios
            self.cuenta_kilometros += distancia 
            return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        max_litros_permitidos = self.capacidad_estanque - self.nivel_estanque
        if litros > max_litros_permitidos:
            return max_litros_permitidos, False
        else:
            self.nivel_estanque += litros
            return self.nivel_estanque, True


if __name__ == "__main__":
    auto = Auto(60, 12)
    print("Autonomía actual:", auto.autonomia())

    auto.llenar_estanque(50)
    print("Estanque después de llenarlo:", auto.nivel_estanque, "litros")

    auto.andar(120, 1)
    print("Estanque después de viajar 1 hora:", auto.nivel_estanque, "litros")


          