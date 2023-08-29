class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,v,t):
        d=v*t
        if self.nivel_estanque*self.rendimiento>=d:
            self.nivel_estanque-=d/self.rendimiento
            self.cuenta_kilometros+=d
            self.kilometraje+=d
            return 0
        else:
            d1=self.nivel_estanque*self.rendimiento
            self.nivel_estanque=0
            self.cuenta_kilometros+=d1
            self.kilometraje+=d1
            d2=d-d1
            return d2
    def autonomia(self):
        q= self.nivel_estanque*self.rendimiento
        return q
    def llenar_estanque(self,L):
        if self.capacidad_estanque<self.nivel_estanque+L:
            maximo=self.capacidad_estanque-self.nivel_estanque
            return str(maximo),False
        else:
            total=self.nivel_estanque+L
            self.nivel_estanque+=L
            return str(total),True
    def __str__(self):
        return str(self.capacidad_estanque) + str(self.rendimiento)

def cantidad_paradas(a,d):
    kilometros=a[0]*a[1]
    d=d-1
    cantidad=d//kilometros
    print(cantidad)

if __name__ == "__main__":
    auto=Auto(100,12)
         