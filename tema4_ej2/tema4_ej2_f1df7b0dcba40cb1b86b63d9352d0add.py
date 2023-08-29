class Auto:
    def __init__(self, capacidad_estanque, rendimiento,nivel_estanque=0):
        self.capacidad_estanque=int(capacidad_estanque)
        self.rendimiento=int(rendimiento)
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=nivel_estanque

    def reinicia_cuentakilometros(self):
        self.cuenta_kilometros=0

    def autonomia(self):
        distancia=self.rendimiento*int(self.nivel_estanque)
        return distancia

    def andar(self,velocidad,tiempo):
        distancia=int(velocidad)*int(tiempo)
        litros_gastados=distancia/self.rendimiento
        self.nivel_estanque=self.nivel_estanque-litros_gastados
        self.kilometraje=self.kilometraje+distancia
        self.cuenta_kilometros=self.cuenta_kilometros+distancia
        if (distancia<=self.autonomia()):
            return 0
        else:
            falto=distancia-autonomia(self)
            return falto

    def llenar_estanque(self,litros):
        litros_finales=int(litros)+int(self.nivel_estanque)
        if(litros_finales>self.capacidad_estanque):
            return {self.capacidad_estanque-self.nivel_estanque,False}
        else:
            self.nivel_estanque=litros_finales
            return {self.nivel_estanque,True}
         