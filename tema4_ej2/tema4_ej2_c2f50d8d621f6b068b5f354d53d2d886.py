class Auto:
    def _init_(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        litros_usados=distancia/self.rendimiento
        if litros_usados<=self.nivel_estanque:
            self.nivel_estanque-=litros_usados
            self.kilometraje+=distancia
            self.cuenta_kilometros+=distancia
            return 0
        else:
            distancia_posible=self.nivel_estanque*self.rendimiento
            self.kilometraje+=distancia_posible
            self.cuenta_kilometros+=distancia_posible
            faltante=distancia-distancia_posible
            return faltante

    def autonomia(self):
        return self.nivel_estanque*self.rendimiento

    def llenar_estanque(self,litros):
        if litros>self.capacidad_estanque:
            return (self.capacidad_estanque,False)
        else:
            self.nivel_estanque=litros
            return (self.nivel_estanque,True)

if _name_ == "_main_":
   print(auto1=Auto(100,12)
    distancia_total=100 # km
    distancia_recorrida=0 # km
    paradas=0 # número de paradas para cargar combustible
    while distancia_recorrida<distancia_total:
        autonomia_actual=auto1.autonomia()
        if autonomia_actual<200: # km antes de quedarse sin bencina
            paradas+=1
            auto1.llenar_estanque(auto1.capacidad_estanque)
        tiempo_restante=(distancia_total-distancia_recorrida)/autonomia_actual*60 # tiempo restante en minutos
        velocidad_promedio=(distancia_total-distancia_recorrida)/tiempo_restante # velocidad promedio para llegar al destino a tiempo
        faltante=auto1.andar(velocidad_promedio,tiempo_restante/60) # tiempo restante en horas
        if faltante>0:
            distancia_recorrida+=auto1.kilometraje-distancia_recorrida+faltante # actualizamos la distancia recorrida con la distancia que faltó por recorrer después de quedarse sin bencina.
            auto1.llenar_estanque(auto1.capacidad_estanque)
            paradas+=1
        else:
            distancia_recorrida+=auto1.kilometraje-distancia_recorrida

    print("Número de paradas para cargar combustible:",paradas)