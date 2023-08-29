class Auto:
    def __init__(self, c, r):
        self.capacidad_estanque= c
        self.rendimiento= r
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
        self.kilometraje =0
    def andar(self,v,t):
        d = v*t
        consumo = d / self.rendimiento
        if consumo > self.nivel_estanque:
            df = self.rendimiento * self.nivel_estanque
            self.nivel_estanque = 0
            self.cuenta_kilometros += d
            return d-df
        else:
            self.cuenta_kilometros +=d
            self.kilometraje +=d
            self.nivel_estanque -= consumo
            return 0


    def reiniciar_cuentakilometros(self):
        if self.cuenta_kilometros!=0:
            self.cuenta_kilometros=0

    def llenar_estanque(self,l):
        self.litros = l
        if l > self.capacidad_estanque:
            return self.capacidad_estanque , False

        elif l <= self.capacidad_estanque and (l + self.nivel_estanque)<= self.capacidad_estanque :
            self.nivel_estanque += l
            return self.nivel_estanque ,True
        else:
            return self.capacidad_estanque , False

    def autonomia(self):
        recorre = self.nivel_estanque * self.rendimiento
        return recorre




if __name__ == "__main__":
    auto=Auto(100,12)
         