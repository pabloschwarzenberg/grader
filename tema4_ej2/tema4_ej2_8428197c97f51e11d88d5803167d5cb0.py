class Auto:
    def _init_(self, capacidad_estanque, consumo_litros_km):
        self.capacidad_estanque = capacidad_estanque
        self.consumo_litros_km = consumo_litros_km
        self.litros_actuales = capacidad_estanque
        self.kilometros_totales = 0
        self.cuenta_kilometros = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        litros_necesarios = distancia / self.consumo_litros_km

        if self.litros_actuales >= litros_necesarios:
            self.litros_actuales -= litros_necesarios
            self.kilometros_totales += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            distancia_posible = self.litros_actuales * self.consumo_litros_km
            self.kilometros_totales += distancia_posible
            self.cuenta_kilometros += distancia_posible
            self.litros_actuales = 0
            return distancia - distancia_posible

    def autonomia(self):
        return self.litros_actuales * self.consumo_litros_km

    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque - self.litros_actuales:
            return (self.capacidad_estanque - self.litros_actuales, False)
        else:
            self.litros_actuales += litros
            return (self.litros_actuales, True)

# Ejemplo de uso
auto = Auto(100, 12)

# Simulamos un viaje de 1000 km
viaje_km = 1000
resto_km = 0
while True:
    resto_km = auto.andar(100, 1)
    if resto_km == 0:
        break
    litros_necesarios = resto_km / auto.consumo_litros_km
    print(f"Detenerse para cargar combustible. Faltan {litros_necesarios} litros. Autonomía actual: {auto.autonomia()} km.")
    litros_a_cargar = auto.capacidad_estanque - auto.litros_actuales
    print(f"Llenando el estanque con {litros_a_cargar} litros.")
    auto.llenar_estanque(litros_a_cargar)

print(f"Se recorrieron {viaje_km} km y se detuvo {viaje_km // resto_km} veces para cargar combustible.")
         