class Auto:

    def __init__(self,capacidad_estanque,rendimiento):

        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,v,t):
        distancia = v/t
        self.kilometraje += distancia
        self.cuenta_kilometros += distancia
        maxima_distancia = self.rendimiento * self.nivel_estanque
        litros_usados = distancia/self.rendimiento
        if distancia <= maxima_distancia:
            self.nivel_estanque += -litros_usados
            return 0
        else:
            self.nivel_estanque = 0
            return distancia-maxima_distancia

    def autonomia(self):
        return float(self.rendimiento * self.nivel_estanque)

    def llenar_estanque(self,cantidad):
        if self.nivel_estanque + cantidad > self.capacidad_estanque:
            return (self.capacidad_estanque-self.nivel_estanque,False)
        else:
            self.nivel_estanque += cantidad
            return (self.nivel_estanque,True)

