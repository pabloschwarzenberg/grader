class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        d=velocidad*tiempo
        k=self.rendimiento*self.nivel_estanque
        if d<=k:
          self.kilometraje=self.kilometraje+d
          self.cuenta_kilometros=self.cuenta_kilometros+d
          self.nivel_estanque=self.nivel_estanque-(d/self.rendimiento)
          return 0
        elif d>k:
          self.kilometraje=self.kilometraje+k
          self.cuenta_kilometros=self.cuenta_kilometros+k
          self.nivel_estanque=self.nivel_estanque-(k/self.rendimiento)
          return(d-k)
    def autonomia(self):
        k=self.rendimiento*self.nivel_estanque
        return k
    def llenar_estanque(self,cant):
        if cant+self.nivel_estanque>self.capacidad_estanque:
            return(self.capacidad_estanque-self.nivel_estanque,False)
        elif cant+self.nivel_estanque<=self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque+cant
            return(self.nivel_estanque,True)


if __name__ == "__main__":
    auto=Auto(100,12)
    v=input('velocidad')
    t=input('tiempo')
    auto.andar(v,t)
    d=v*t
    print(d//auto.autonomia())