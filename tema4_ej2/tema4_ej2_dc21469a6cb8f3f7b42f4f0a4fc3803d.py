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
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            distancia_faltante = self.rendimiento * self.nivel_estanque
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            return distancia - distancia_faltante   
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento   
    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False
if __name__ == "__main__":
    auto = Auto(100, 12)   
    velocidad = 100  
    tiempo = 5   
    detenciones = 0   
    while True:
        faltante = auto.andar(velocidad, tiempo)
        if faltante > 0:
            litros_necesarios = faltante / auto.rendimiento
            litros_disponibles, exito = auto.llenar_estanque(litros_necesarios)
            if exito:
                detenciones += 1
                continue
            else:
                break
        else:
            break   
    print("Numero de detenciones necesarias:", detenciones)         