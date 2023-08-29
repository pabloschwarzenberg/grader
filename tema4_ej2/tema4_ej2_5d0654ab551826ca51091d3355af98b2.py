class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.nivel_estanque = 0
        self.cuenta_kilometros=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,velocidad,tiempo_de_viaje):
        if self.nivel_estanque - (velocidad * tiempo_de_viaje / self.rendimiento)<0:
            km_faltantes = (velocidad * tiempo_de_viaje / self.rendimiento)-self.nivel_estanque
            self.nivel_estanque = 0
            self.kilometraje += velocidad * tiempo_de_viaje - km_faltantes
            self.cuenta_kilometros += velocidad * tiempo_de_viaje - km_faltantes
            return km_faltantes
        else:
            self.cuenta_kilometros += velocidad * tiempo_de_viaje
            self.kilometraje += velocidad * tiempo_de_viaje
            self.nivel_estanque -= velocidad * tiempo_de_viaje / self.rendimiento
            return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque > self.capacidad_estanque:
            return self.capacidad_estanque - self.nivel_estanque, False
        else:
            self.nivel_estanque += litros
            return self.nivel_estanque, True

if __name__ == "__main__":
    auto=Auto(100,12)
         