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
            litros_posibles = self.capacidad_estanque - self.nivel_estanque
            return litros_posibles, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    viaje1 = auto.andar(80, 2)  
    print("Kilómetros recorridos:", auto.kilometraje)
    print("Cuenta kilómetros:", auto.cuenta_kilometros)
    print("Autonomía restante:", auto.autonomia())

    auto.reiniciar_cuentakilometros()

    viaje2 = auto.andar(100, 1.5)  
    print("Kilómetros recorridos:", auto.kilometraje)
    print("Cuenta kilómetros:", auto.cuenta_kilometros)
    print("Autonomía restante:", auto.autonomia())

    litros, exito = auto.llenar_estanque(50)  
    if exito:
        print("Litros actuales:", auto.nivel_estanque)
    else:
        print("No se pudo llenar el estanque por completo. Se llenaron", litros, "litros.")

         