class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    def andar(self,velocidad,tiempo):
        distancia_recorrida = velocidad*tiempo
        self.nivel_estanque = self.nivel_estanque-(distancia_recorrida/self.rendimiento)
        self.kilometraje = self.kilometraje + distancia_recorrida
        self.cuenta_kilometros = self.cuenta_kilometros + distancia_recorrida
        if self.nivel_estanque<0:
            return 'Combustible insuficiente. Faltaron {} kilometros por recorrer.'.format(distancia_recorrida-(self.rendimiento*self.capacidad_estanque))
        else:
            return 0
    def autonomia(self):
        self.distancia_maxima = self.rendimiento*self.nivel_estanque
        return self.distancia_maxima

    def llenar_estanque(self,litros):
        n = self.nivel_estanque + litros
        if n>self.capacidad_estanque:
            return (self.capacidad_estanque,False)
        else:
            self.nivel_estanque = n
            return (self.nivel_estanque,True)

if __name__ == "__main__":
    auto=Auto(100,12)
         