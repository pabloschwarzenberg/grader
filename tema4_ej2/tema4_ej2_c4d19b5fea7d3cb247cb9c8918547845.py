class Auto:

    def __init__(self,capacidad_estanque,rendimiento):

        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento


    def reiniciar_cuentakilometros(self):

        self.cuenta_kilometros = 0


    def andar(self,velocidad,tiempo_viaje):


        self.kilometraje = velocidad*tiempo_viaje
        if self.nivel_estanque == 0:

            self.nivel_estanque = self.capacidad_estanque-(self.kilometraje/self.rendimiento)

        else:
            self.nivel_estanque = self.nivel_estanque-(self.kilometraje/self.rendimiento)
            
        self.cuenta_kilometros = self.kilometraje



        if self.nivel_estanque < 0:

            return -(self.nivel_estanque*self.rendimiento)

        else:

            return 0



    def autonomia(self):

        aut = self.nivel_estanque*self.rendimiento

        return aut


    def llenar_estanque(self,litros):

        if self.capacidad_estanque >= litros + self.nivel_estanque:
            self.nivel_estanque = litros+self.nivel_estanque

            return (self.nivel_estanque,True)

        else:

            return(self.capacidad_estanque,False)


    def veces_cargar(self):

        f = self.capacidad_estanque*self.rendimiento

        if self.kilometraje != 0:

            if self.kilometraje > f:

                k = self.kilometraje-1//f
                k = k+1

            else:

                k = f -1 //self.kilometraje
                k = k+1

        return k
            

            
if __name__ == "__main__":
    auto=Auto(100,12)
         