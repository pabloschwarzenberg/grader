class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometro(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        distancia = velocidad * tiempo
        bencia_necesaria = distancia/self.rendimiento
        if self.nivel_estanque >= bencia_necesaria:
            self.kilometraje = distancia
            self.nivel_estanque -= bencia_necesaria
            return 0
        else:
            distancia_recor = self.rendimiento * self.nivel_estanque
            distancia_faltante = distancia - distancia_recor
            return distancia_faltante

    def autonomia(self):
        distancia_actual = self.nivel_estanque * self.rendimiento
        return distancia_actual

    def llenar_estanque(self,litros):
        litrosactuales = self.nivel_estanque + litros
        if self.capacidad_estanque < litrosactuales:
            return self.capacidad_estanque,False
        else:
            self.nivel_estanque = litrosactuales
            return self.nivel_estanque,True