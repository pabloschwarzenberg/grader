class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometro=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento    
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return self.cuenta_kilometro
    def andar(self, velocidad, tiempo):
        kilometros=velocidad*tiempo
        litros_gastados=kilometros/self.rendimiento
        self.kilometraje=self.kilometraje+kilometros
        self.cuenta_kilometro=self.cuenta_kilometro+kilometros
        self.nivel_estanque=self.nivel_estanque-litros_gastados
        if self.nivel_estanque>=0:
          return str(0)
        elif self.nivel_estanque<0:
          return str(self.cuenta_kilometro)
        return self.nivel_estanque
    def autonomia(self):
        recorri=self.nivel_estanque*self.rendimiento
        return recorri   
    def llenar_estanque(self,litros):
        if litros==60:
            self.nivel_estanque=60
        if (litros+self.nivel_estanque)<100:
            self.nivel_estanque=self.nivel_estanque*litros
            return self.capacidad_estanque, True
        else:
            return self.nivel_estanque,False
    pass       
  