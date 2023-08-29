class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(' ')
        self.fecha = partes[0]
        self.hora = partes[1]

    def cambiar(self, parametro):
        partes = parametro.split('=')
        tipo_parametro = partes[0].strip().lower()
        valor_parametro = partes[1].strip()

        if tipo_parametro == 'dd':
            dia = int(valor_parametro)
            if 1 <= dia <= 31:
                self.fecha = self._actualizar_fecha(dia, 'dd')
            else:
                print("Día inválido")
        elif tipo_parametro == 'mm':
            mes = int(valor_parametro)
            if 1 <= mes <= 12:
                self.fecha = self._actualizar_fecha(mes, 'mm')
            else:
                print("Mes inválido")
        elif tipo_parametro == 'aaaa':
            anio = int(valor_parametro)
            if 1900 <= anio <= 2100:
                self.fecha = self._actualizar_fecha(anio, 'aaaa')
            else:
                print("Año inválido")
        elif tipo_parametro == 'hh':
            hora = int(valor_parametro)
            if 0 <= hora <= 23:
                self.hora = self._actualizar_hora(hora, 'hh')
            else:
                print("Hora inválida")
        elif tipo_parametro == 'mm':
            minuto = int(valor_parametro)
            if 0 <= minuto <= 59:
                self.hora = self._actualizar_hora(minuto, 'mm')
            else:
                print("Minuto inválido")
        elif tipo_parametro == 'ss':
            segundo = int(valor_parametro)
            if 0 <= segundo <= 59:
                self.hora = self._actualizar_hora(segundo, 'ss')
            else:
                print("Segundo inválido")
        else:
            print("Parámetro inválido")

    def _actualizar_fecha(self, valor, tipo):
        partes = self.fecha.split('/')
        if tipo == 'dd':
            partes[0] = str(valor).zfill(2)
        elif tipo == 'mm':
            partes[1] = str(valor).zfill(2)
        elif tipo == 'aaaa':
            partes[2] = str(valor).zfill(4)
        return '/'.join(partes)

    def _actualizar_hora(self, valor, tipo):
        partes = self.hora.split(':')
        if tipo == 'hh':
            partes[0] = str(valor).zfill(2)
        elif tipo == 'mm':
            partes[1] = str(valor).zfill(2)
        elif tipo == 'ss':
            partes[2] = str(valor).zfill(2)
        return ':'.join(partes)

    def __str__(self):
        return f"{self.fecha} {self.hora}"


# Ejemplo de uso
fecha_hora = FechaHora()

fecha_hora.fijarFecha("01/01/2023")
fecha_hora.fijarHora("12:30:00")
print(fecha_hora)  # Salida: 01/01/2023 12:30:00

fecha_hora.fijarFechaHora("15/06/2023 10:45:30")
print(fecha_hora)  # Salida: 15/06/2023 10:45:30

fecha_hora.cambiar("dd=25")
fecha_hora.cambiar("mm=07")
fecha_hora.cambiar("aaaa=2022")
print(fecha_hora)  # Salida: 25/07/2022 10:45:30

fecha_hora.cambiar("hh=18")
fecha_hora.cambiar("mm=55")
fecha_hora.cambiar("ss=40")
print(fecha_hora)  # Salida: 25/07/2022 18:55:40

fecha_hora.fijarHora("12:30:00")
print(fecha_hora)  # Salida: 01/01/2023 12:30:00
