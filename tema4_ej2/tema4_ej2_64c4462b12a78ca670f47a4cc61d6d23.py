class Auto:
    def __init__(self,capacidad,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0 
        self.capacidad_estanque = capacidad
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,v,t):
        d = v * t #distancia
        litros = d / self.rendimiento #litros consumidos en d
        if litros <= self.nivel_estanque:
            self.nivel_estanque -= litros
            self.kilometraje += d
            self.cuenta_kilometros += d
            return 0
        else:
            self.nivel_estanque = 0
            d = self.nivel_estanque * self.rendimiento
            self.kilometraje += d
            self.cuenta_kilometros += d
            l = litros-self.nivel_estanque
            return l

    def autonomia(self):
        a = self.nivel_estanque * self.rendimiento
        return a

    def llenar_estanque(self,l):
        if self.nivel_estanque + l <= self.capacidad_estanque:
            self.nivel_estanque += l
            return (self.nivel_estanque,True)
        else:
            a = self.nivel_estanque + l
            b = self.capacidad_estanque - a
            c = a - b
            d = l - a
            return (d, False)
        

if __name__ == "__main__":
    auto=Auto(100,12)
         