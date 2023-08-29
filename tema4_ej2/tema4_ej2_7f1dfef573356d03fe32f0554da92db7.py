class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    def andar(self,v,t):
        self.nivel_estanque -= v*t* self.rendimiento
        if self.nivel_estanque < 0:
            a = int((-1 * self.nivel_estanque)/self.rendimiento)
            self.nivel_estanque = 0
            self.kilometraje += v*t - a
            self.cuenta_kilometros = v*t - a
            return a
        else:
            self.kilometraje += v*t
            self.cuenta_kilometros = v*t
            return 0
    def autonomia(self):
        return self.rendimiento * self.nivel_estanque
    def llenar_estanque(self,L):
        if self.nivel_estanque + L <= self.capacidad_estanque:
            self.nivel_estanque += L
            return self.nivel_estanque,True
        else:
            return self.capacidad_estanque,False
         