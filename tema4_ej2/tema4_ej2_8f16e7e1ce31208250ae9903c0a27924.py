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
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            litros_maximos = self.capacidad_estanque - self.nivel_estanque
            return litros_maximos, False


# Ejemplo de uso
auto = Auto(capacidad_estanque=100, rendimiento=12)

velocidad = 80  # km/h
tiempo = 4  # horas

distancia_viaje = velocidad * tiempo
litros_necesarios = distancia_viaje / auto.rendimiento

num_paradas = 0
while litros_necesarios > 0:
    autonomia_actual = auto.autonomia()
    
    if litros_necesarios <= autonomia_actual:
        auto.andar(velocidad, tiempo)
        break
    
    litros_maximos, _ = auto.llenar_estanque(auto.capacidad_estanque)
    litros_necesarios -= litros_maximos
    num_paradas += 1

print("Número de paradas necesarias:", num_paradas)



# clase fechahora

from datetime import datetime

class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        if self.fecha and self.hora:
            return self.fecha.strftime('%Y/%m/%d') + ' ' + self.hora.strftime('%H:%M:%S')
        else:
            return ""

    def fijarFecha(self, fecha):
        try:
            self.fecha = datetime.strptime(fecha, '%d/%m/%Y')
        except ValueError:
            try:
                self.fecha = datetime.strptime(fecha, '%d-%m-%Y')
            except ValueError:
                print('Formato de fecha incorrecto')

    def fijarHora(self, hora):
        try:
            self.hora = datetime.strptime(hora, '%H:%M:%S')
        except ValueError:
            print('Formato de hora incorrecto')

    def fijarFechaHora(self, fechahora):
        try:
            fecha_hora = datetime.strptime(fechahora, '%d-%m-%Y %H:%M:%S')
            self.fecha = fecha_hora
            self.hora = fecha_hora
        except ValueError:
            try:
                fecha_hora = datetime.strptime(fechahora, '%d/%m/%Y %H:%M:%S')
                self.fecha = fecha_hora
                self.hora = fecha_hora
            except ValueError:
                print('Formato de fecha y hora incorrecto')

    def cambiar(self, parte):
        parte = parte.replace(' ', '')
        if '=' in parte:
            parametro, valor = parte.split('=')
            if parametro == 'dd':
                if 1 <= int(valor) <= 31:
                    self.fecha = self.fecha.replace(day=int(valor))
                else:
                    print('Día inválido')
            elif parametro == 'mm':
                if 1 <= int(valor) <= 12:
                    self.fecha = self.fecha.replace(month=int(valor))
                else:
                    print('Mes inválido')
            elif parametro == 'aaaa':
                if int(valor) >= 1:
                    self.fecha = self.fecha.replace(year=int(valor))
                else:
                    print('Año inválido')
            elif parametro == 'HH':
                if 0 <= int(valor) <= 23:
                    self.hora = self.hora.replace(hour=int(valor))
                else:
                    print('Hora inválida')
            elif parametro == 'MM':
                if 0 <= int(valor) <= 59:
                    self.hora = self.hora.replace(minute=int(valor))
                else:
                    print('Minuto inválido')
            elif parametro == 'SS':
                if 0 <= int(valor) <= 59:
                    self.hora = self.hora.replace(second=int(valor))
                else:
                    print('Segundo inválido')
            else:
                print('Parámetro desconocido')
        else:
            print('Formato de cambio incorrecto')

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)
    fh.cambiar("mm=10")
    print(fh)
    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)