class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
        
    def reinciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,velocidad,tiempo):
        self.nivel_estanque = self.nivel_estanque - velocidad*tiempo/self.rendimiento
        self.cuenta_kilometros += velocidad*tiempo
        self.kilometraje += self.cuenta_kilometros
        if self.nivel_estanque<0:
            return abs(self.nivel_estanque)
        else:
            return 0
        

    def autonomia(self):
        self.cuantos_km = self.nivel_estanque*self.rendimiento

    def llenar_estanque(self,cant_litros):
        self.nivel_estanque += cant_litros
        if self.nivel_estanque>self.capacidad_estanque:
            return "{},{}".format(self.capacidad_estanque-(self.nivel_estanque - cant_litros),False)
        else:
            return "{},{}".format(self.nivel_estanque,True)
if __name__ == "__main__":
  pass
         