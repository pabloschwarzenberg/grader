class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        litros_gastados = distancia / self.rendimiento
        if litros_gastados > self.nivel_estanque:
            litros_faltantes  = litros_gastados - self.nivel_estanque
            self.nivel_estanque = 0
            km_por_recorrer = self.rendimiento * litros_faltantes
            km_recorridos = distancia - km_por_recorrer
            self.kilometraje += km_recorridos
            self.cuenta_kilometros += km_recorridos
            return km_por_recorrer
        else:
            self.cuenta_kilometros += distancia
            self.kilometraje += distancia
            self.nivel_estanque -= litros_gastados
            return 0

    def autonomia(self):
        km_puede_recorrer = self.rendimiento * self.nivel_estanque
        return km_puede_recorrer

    def llenar_estanque(self, cant_litros):
        if cant_litros + self.nivel_estanque > self.capacidad_estanque:
            capacidad_restante = self.capacidad_estanque - self.nivel_estanque
            return [capacidad_restante, False]
        else:
            self.nivel_estanque += cant_litros
            return [self.nivel_estanque, True]

if __name__ == "__main__":
    auto=Auto(100,12)
         