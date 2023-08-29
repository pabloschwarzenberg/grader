class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,velocidad,tiempo_viaje):
        a = velocidad*tiempo_viaje
        c = (self.nivel_estanque)*(self.rendimiento)
        g = a/(self.rendimiento)
        if c < a:
            b = a - c
            return b
        if c >= a:
            self.nivel_estanque = self.nivel_estanque - g
            self.kilometraje = self.kilometraje + a
            self.cuenta_kilometros = self.cuenta_kilometros + a
            return 0

    def autonomia(self):
        a = (self.nivel_estanque)*(self.rendimiento)

        return a
    def llenar_estanque(self,nueva_carga):
        if self.nivel_estanque == self.capacidad_estanque:
            return 0, False
        elif self.nivel_estanque == 0 and (self.nivel_estanque + nueva_carga) <= self.capacidad_estanque:
            d = self.nivel_estanque + nueva_carga
            self.nivel_estanque = self.nivel_estanque + nueva_carga
            return d, True
        elif self.nivel_estanque != 0 and (self.nivel_estanque + nueva_carga) <= self.capacidad_estanque:
            d = self.nivel_estanque + nueva_carga
            self.nivel_estanque = self.nivel_estanque + nueva_carga
            return d,True
        elif self.nivel_estanque != 0 and (self.nivel_estanque + nueva_carga) > self.capacidad_estanque:
            e = self.capacidad_estanque - self.nivel_estanque
            return e, False
if __name__ == "__main__":
    auto=Auto(100,12)
         