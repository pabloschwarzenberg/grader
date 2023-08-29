class Auto:

    def __init__(self,capacidad_estanque,rendimiento):

        self.kilometraje=0

        self.cuenta_kilometros=0

        self.capacidad_estanque=capacidad_estanque

        self.nivel_estanque=0

        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):

        self.cuenta_kilometros=0

    def andar(self,v,t):

        self.kilometraje=v*t

        self.nivel_estanque-=self.kilometraje/self.rendimiento

    def autonomia(self):

        a=self.rendimiento*self.nivel_estanque

        return a

    def llenar_estanque(self,l):

        if self.nivel_estanque+l<=self.capacidad_estanque:

            self.nivel_estanque+=l

            return self.nivel_estanque,True

        else:

            return self.capacidad_estanque,False

    def cuantascargas(self,k):

        c=(k//(self.rendimiento*self.capacidad_estanque))+1

        return c

if __name__ == "__main__":

    auto=Auto(100,12)

    print(auto.cuantascargas(1300))