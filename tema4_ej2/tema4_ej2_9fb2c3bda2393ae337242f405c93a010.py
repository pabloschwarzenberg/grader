class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuenta_kilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo_de_viaje):
        self.nivel_estanque=(velocidad*tiempo_de_viaje)*self.rendimiento
        self.kilometraje+=velocidad*tiempo_de_viaje
        d=velocidad*tiempo_de_viaje
        dmax=self.nivel_estanque*self.rendimiento
        if d<=dmax:
            return 0
        if d>dmax:
            D=d-dmax
            return D
    def autonomia(self):
        d=self.rendimiento*self.nivel_estanque
        return d
    def llenar_estanque(self,litros):
        ln=self.nivel_estanque+litros
        if ln<=self.capacidad_estanque:
            self.nivel_estanque = ln
            tupla=(ln,True)
            return tupla
        if ln>self.capacidad_estanque:
            tupla=(self.capacidad_estanque-self.nivel_estanque,False)
   


          
          

if __name__ == "__main__":
    auto=Auto(100,12)
    d=int(input("Ingrese distancia del viaje: "))

    L=d/auto.rendimiento

    if L<=auto.capacidad_estanque:
        print ("Es necesario llenar 1 una vez el estanque")
    else:
        auto.llenar_estanque(100)
        Dmax=auto.autonomia()
        contador=1
        D = d - Dmax
        while D>=Dmax:
            Dmax+=Dmax
            D=d-Dmax

            contador+=1
        print ("Es necesario llenar {0} veces el estanque".format(contador))
         