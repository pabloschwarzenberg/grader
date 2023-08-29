class Auto:
    def __init__(self,capacidad_estanque,rendimiento,cuenta_kilometros=0,nivel_estanque=0,kilometraje=0):
        self.kilometraje=kilometraje
        self.cuenta_kilometros=cuenta_kilometros
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=nivel_estanque
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self,cuenta_kilometros):
        self.cuenta_kilometros=0
        return self.cuenta_kilometros
    def andar(self,velocidad,tiempo):
        distancia_recorrer=velocidad*tiempo
        litros_necesita=distancia_recorrer/self.rendimiento
        if litros_necesita<=self.nivel_estanque:
            self.nivel_estanque=self.nivel_estanque-litros_necesita
            self.kilometraje=self.kilometraje+distancia_recorrer
            self.cuenta_kilometros=distancia_recorrer+self.cuenta_kilometros
            return 0
        else:
            recorrio=self.nivel_estanque*self.rendimiento
            self.kilometraje=self.kilometraje+recorrio
            self.cuenta_kilometros=self.cuenta_kilometros+recorrio
            falta_recorrer=distancia_recorrer-recorrio
            self.nivel_estanque=0
            return falta_recorrer
    def autonomia(self):
        puede_recorrer=self.rendimiento*self.nivel_estanque
        return puede_recorrer
    def llenar_estanque(self,llenado):
        cabe=self.capacidad_estanque-self.nivel_estanque
        if llenado>cabe:
            return cabe,False
        else:
            self.nivel_estanque=self.nivel_estanque+llenado
            return self.nivel_estanque,True
    def __str__(self):
        return "Auto:\n Kilometraje: "+str(self.kilometraje)+"\n Cuenta kilómetros: "+str(self.cuenta_kilometros)+"\n Rendimiento: "+str(self.rendimiento)+"\n Capacidad Estanque: "+str(self.capacidad_estanque)+"\n Nivel Estanque: "+str(self.nivel_estanque)
if __name__ == "__main__":
    auto=Auto(100,12)
         