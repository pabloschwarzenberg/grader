class Auto:

    def __init__(self, _capacidad, _rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = _capacidad
        self.nivel_estanque = 0
        self.rendimiento = _rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        bencina_gastada = distancia / self.rendimiento
        bencina_restante = self.nivel_estanque - bencina_gastada
        self.kilometraje += distancia
        self.cuenta_kilometros += distancia
        if bencina_restante > 0:
            return 0
        elif bencina_restante < 0:
            distancia_restante = self.rendimiento * bencina_restante
            return abs(distancia_restante)

    def autonomia(self):
        distancia = self.rendimiento * self.nivel_estanque
        return distancia

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque:
            self.nivel_estanque += litros
            ret = {self.nivel_estanque, True}
            return ret
        else:
            self.nivel_estanque = self.capacidad_estanque
            ret = {self.capacidad_estanque, False}
            return ret

         