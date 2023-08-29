class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        litros_necesarios = distancia / self.rendimiento

        if litros_necesarios <= self.nivel_estanque:
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque:
            self.nivel_estanque = litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


auto = Auto(100, 12)

velocidad_viaje = 100 
tiempo_viaje = 6

viaje_total = 500

detenciones_carga = 0  

while viaje_total > 0:
    distancia_faltante = auto.andar(velocidad_viaje, tiempo_viaje)

    if distancia_faltante > 0:
        detenciones_carga += 1
        litros_cargados, exito_carga = auto.llenar_estanque(auto.capacidad_estanque)
        if not exito_carga:
            break
        viaje_total -= distancia_faltante
    else:
        viaje_total -= auto.cuenta_kilometros
        auto.reiniciar_cuentakilometros()

print("Cantidad de detenciones para cargar combustible:", detenciones_carga)
    