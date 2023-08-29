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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia - distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            litros_disponibles = self.capacidad_estanque - self.nivel_estanque
            return litros_disponibles, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    
    # Ejemplo de uso del auto
    auto.reiniciar_cuentakilometros()
    distancia_recorrida = 0
    veces_detenido = 0

    while distancia_recorrida < 1000:
        tiempo_viaje = int(input("Ingrese el tiempo de viaje en horas: "))
        velocidad = int(input("Ingrese la velocidad en km/h: "))
        
        distancia_faltante = auto.andar(velocidad, tiempo_viaje)
        distancia_recorrida += distancia_faltante

        if distancia_faltante > 0:
            veces_detenido += 1
            litros_disponibles, _ = auto.llenar_estanque(100)
            print("Te quedaste sin combustible. Faltaron ", distancia_faltante, "km para terminar el viaje.")
            print("Llenando el estanque con", litros_disponibles, "litros.")
    
    print("Viaje finalizado. Te detuviste a cargar combustible ", veces_detenido, "veces.")
