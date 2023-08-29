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

        if litros_necesarios > self.nivel_estanque:
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return distancia_faltante
        else:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        litros_permitidos = min(cantidad_litros, self.capacidad_estanque - self.nivel_estanque)
        self.nivel_estanque += litros_permitidos
        return litros_permitidos, litros_permitidos == cantidad_litros


if __name__ == "__main__":
    auto = Auto(60, 12)
    
    litros_permitidos, exito = auto.llenar_estanque(60)  # Intento llenar el estanque con 60 litros (mayor que la capacidad)
    print("Estanque:", auto.nivel_estanque, "litros")
    
    autonomia = auto.autonomia()
    print("Autonomía:", autonomia, "km")
    
    distancia_faltante = auto.andar(120, 1)
    print("Estanque:", auto.nivel_estanque, "litros")
    
    print("Distancia faltante:", distancia_faltante, "km")