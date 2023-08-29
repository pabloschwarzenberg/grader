class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        if parametro.startswith("dd="):
            nuevo_dia = parametro[3:]
            if self.validarDia(int(nuevo_dia)):
                self.fecha = self.fecha[:8] + nuevo_dia
            else:
                print("Día inválido.")
        elif parametro.startswith("mm="):
            nuevo_mes = parametro[3:]
            if self.validarMes(int(nuevo_mes)):
                self.fecha = self.fecha[:5] + nuevo_mes + self.fecha[7:]
            else:
                print("Mes inválido.")
        elif parametro.startswith("aaaa="):
            nuevo_anio = parametro[5:]
            if self.validarAnio(int(nuevo_anio)):
                self.fecha = nuevo_anio + self.fecha[4:]
            else:
                print("Año inválido.")
        elif parametro.startswith("HH="):
            nueva_hora = parametro[3:]
            if self.validarHora(int(nueva_hora)):
                self.hora = nueva_hora + self.hora[2:]
            else:
                print("Hora inválida.")
        elif parametro.startswith("MM="):
            nuevos_minutos = parametro[3:]
            if self.validarMinutos(int(nuevos_minutos)):
                self.hora = self.hora[:3] + nuevos_minutos + self.hora[5:]
            else:
                print("Minutos inválidos.")
        elif parametro.startswith("SS="):
            nuevos_segundos = parametro[3:]
            if self.validarSegundos(int(nuevos_segundos)):
                self.hora = self.hora[:6] + nuevos_segundos
            else:
                print("Segundos inválidos.")
        else:
            print("Parámetro inválido.")

    def validarDia(self, dia):
        return 1 <= dia <= 31

    def validarMes(self, mes):
        return 1 <= mes <= 12

    def validarAnio(self, anio):
        return anio >= 0

    def validarHora(self, hora):
        return 0 <= hora <= 23

    def validarMinutos(self, minutos):
        return 0 <= minutos <= 59

    def validarSegundos(self, segundos):
        return 0 <= segundos <= 59

    def __str__(self):
        return f"{self.fecha} {self.hora}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha("25/06/2023")
fecha_hora.fijarHora("12:30:45")
print(fecha_hora)  # Imprime: 25/06/2023 12:30:45

fecha_hora.cambiar("dd=26")
fecha_hora.cambiar("HH=20")
print(fecha_hora)  # Imprime: 26/06/2023 20:30:45

