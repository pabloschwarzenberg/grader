class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        self.fecha, self.hora = fecha_hora.split(" ")

    def cambiar(self, parametro):
        if "=" in parametro:
            key, value = parametro.split("=")
            if key == "dd":
                if not self._validar_dia(int(value)):
                    print("Error: Día inválido")
                else:
                    self.fecha = self._reemplazar_valor(self.fecha, 0, 2, value)
            elif key == "mm":
                if not self._validar_mes(int(value)):
                    print("Error: Mes inválido")
                else:
                    self.fecha = self._reemplazar_valor(self.fecha, 3, 5, value)
            elif key == "aaaa":
                if not self._validar_año(int(value)):
                    print("Error: Año inválido")
                else:
                    self.fecha = self._reemplazar_valor(self.fecha, 6, 10, value)
            elif key == "HH":
                if not self._validar_hora(int(value)):
                    print("Error: Hora inválida")
                else:
                    self.hora = self._reemplazar_valor(self.hora, 0, 2, value)
            elif key == "MM":
                if not self._validar_minuto(int(value)):
                    print("Error: Minuto inválido")
                else:
                    self.hora = self._reemplazar_valor(self.hora, 3, 5, value)
            elif key == "SS":
                if not self._validar_segundo(int(value)):
                    print("Error: Segundo inválido")
                else:
                    self.hora = self._reemplazar_valor(self.hora, 6, 8, value)
            else:
                print("Error: Parámetro inválido")
        else:
            print("Error: Formato de parámetro incorrecto")

    def _validar_dia(self, dia):
        return 1 <= dia <= 31

    def _validar_mes(self, mes):
        return 1 <= mes <= 12

    def _validar_año(self, año):
        return año >= 1

    def _validar_hora(self, hora):
        return 0 <= hora <= 23

    def _validar_minuto(self, minuto):
        return 0 <= minuto <= 59

    def _validar_segundo(self, segundo):
        return 0 <= segundo <= 59

    def _reemplazar_valor(self, cadena, inicio, fin, nuevo_valor):
        return cadena[:inicio] + nuevo_valor + cadena[fin+1:]

    def __str__(self):
        return f"{self.fecha} {self.hora}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha("01/01/2022")
fecha_hora.fijarHora("12:30:45")
print(fecha_hora)  # Salida: 01/01/2022 12:30:45

fecha_hora.fijarFechaHora("02/02/2023 15:45:30")
print(fecha_hora)  # Salida: 02/02/2023