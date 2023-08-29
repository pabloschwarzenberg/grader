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
            km_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - km_faltantes
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return km_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


# Ejemplo de uso
if __name__ == "__main__":
    auto = Auto(capacidad_estanque=100, rendimiento=12)
    viaje = [(80, 2), (60, 3), (100, 1)]  # Lista de tuplas (velocidad, tiempo)

    detenciones = 0
    for velocidad, tiempo in viaje:
        km_faltantes = auto.andar(velocidad, tiempo)
        if km_faltantes > 0:
            detenciones += 1
            litros_necesarios = km_faltantes / auto.rendimiento
            max_litros, _ = auto.llenar_estanque(litros_necesarios)
            print(f"No hay suficiente combustible. Debes detenerte a cargar máximo {max_litros} litros.")
    
    print(f"Debes detenerte a cargar combustible {detenciones} veces durante el viaje.")
