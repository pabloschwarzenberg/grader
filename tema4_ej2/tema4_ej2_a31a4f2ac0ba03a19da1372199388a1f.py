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
        km_por_recorrer = velocidad * tiempo
        litros_necesarios = km_por_recorrer / self.rendimiento

        if self.nivel_estanque < litros_necesarios:
            km_que_alcanzan = self.nivel_estanque * self.rendimiento
            km_que_faltan = km_por_recorrer - km_que_alcanzan
            self.nivel_estanque = 0
            self.kilometraje += km_que_alcanzan
            self.cuenta_kilometros += km_que_alcanzan
            return km_que_faltan

        else:
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += km_por_recorrer
            self.cuenta_kilometros += km_por_recorrer
            return 0

    def autonomia(self):
        kilometros_que_puede_recorrer = self.nivel_estanque * self.rendimiento
        return kilometros_que_puede_recorrer

    def llenar_estanque(self, litros):
        quedaria = self.nivel_estanque + litros

        if quedaria > self.capacidad_estanque:
            maximo = self.capacidad_estanque - self.nivel_estanque
            tupla = (maximo, "False")
            return tupla

        else:
            self.nivel_estanque = quedaria
            tupla = (quedaria, "True")
            return tupla
if __name__ == "__main__":
    auto=Auto(100,12)
    
         