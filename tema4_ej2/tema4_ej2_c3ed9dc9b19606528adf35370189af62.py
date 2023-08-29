class Auto:
    def __init__(self,capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo_viaje):
        distancia_recorrer=velocidad*tiempo_viaje
        distancia_maxima=self.nivel_estanque*self.rendimiento
        if distancia_recorrer>distancia_maxima:
            distancia_falta=distancia_recorrer-distancia_maxima
            litros_usados=distancia_recorrer/self.rendimiento
            self.nivel_estanque=0
            self.kilometraje+=distancia_maxima
            self.cuenta_kilometros+=distancia_maxima
            return distancia_falta
        else:
            litros_usados=distancia_recorrer/self.rendimiento
            self.nivel_estanque-=litros_usados
            self.kilometraje+=distancia_recorrer
            self.cuenta_kilometros+=distancia_recorrer
            return 0
    def autonomia(self):
        distancia_maxima=self.nivel_estanque*self.rendimiento
        return distancia_maxima
    def llenar_estanque(self,cant_litros):
        estanque_restante=self.capacidad_estanque-self.nivel_estanque
        if cant_litros>estanque_restante:
            return estanque_restante,False
        else:
            self.nivel_estanque+=cant_litros
            return self.nivel_estanque,True
#auto=Auto(100,12)
#print(auto.andar(1,120))
        
        
