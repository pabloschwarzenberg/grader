class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,ve,t):
        dist=ve*t
        l=dist/self.rendimiento
        if self.rendimiento*self.nivel_estanque >= dist:
          self.nivel_estanque -= dist/self.rendimiento
          self.kilometraje = self.kilometraje + dist
          self.cuenta_kilometros += dist
          return 0 #self.nivel_estanque
        else:
          distancia_recorrida = self.nivel_estanque*self.rendimiento
          self.nivel_estanque = 0
          self.kilometraje += distancia_recorrida
          self.cuenta_kilometros += dist
          return dist - distancia_recorrida

    def autonomia(self):
        k=self.rendimiento*self.nivel_estanque
        return k

    def llenar_estanque(self, c_l):
        nuevo = self.nivel_estanque + c_l
        if nuevo > self.capacidad_estanque:
           return(self.capacidad_estanque,False)
        else:
            self.nivel_estanque = nuevo
            return(self.nivel_estanque,True)

auto=Auto(100,12)