class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha):
        self.fecha = fecha.replace("-", "/")

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fecha = fecha.replace("-", "/")
        self.hora = hora

    def cambiar(self, parametro):
        tipo_parametro, valor = parametro.split('=')
        tipo_parametro = tipo_parametro.strip().lower()
        valor = valor.strip()

        if tipo_parametro == "dd":
            self.actualizar_dia(valor)
        elif tipo_parametro == "mm":
            self.actualizar_mes(valor)
        elif tipo_parametro == "aaaa":
            self.actualizar_anio(valor)
        elif tipo_parametro == "hh":
            self.actualizar_hora(valor)
        elif tipo_parametro == "min":
            self.actualizar_minuto(valor)
        elif tipo_parametro == "ss":
            self.actualizar_segundo(valor)
        else:
            print("Parámetro inválido:", tipo_parametro)

    def actualizar_dia(self, dia):
        if self.validar_dia(dia):
            self.fecha = self.fecha[:7] + dia + self.fecha[8:]
        else:
            print("Valor inválido para el parámetro dd")

    def actualizar_mes(self, mes):
        if self.validar_mes(mes):
            self.fecha = self.fecha[:5] + mes + self.fecha[7:]
        else:
            print("Valor inválido para el parámetro mm")

    def actualizar_anio(self, anio):
        if self.validar_anio(anio):
            self.fecha = self.fecha[:0] + anio + self.fecha[3:]
        else:
            print("Valor inválido para el parámetro aaaa")

    def actualizar_hora(self, hora):
        if self.validar_hora(hora):
            self.hora = hora + self.hora[2:]
        else:
            print("Valor inválido para el parámetro hh")

    def actualizar_minuto(self, minuto):
        if self.validar_minuto(minuto):
            self.hora = self.hora[:3] + minuto + self.hora[5:]
        else:
            print("Valor inválido para el parámetro min")

    def actualizar_segundo(self, segundo):
        if self.validar_segundo(segundo):
            self.hora = self.hora[:6] + segundo
        else:
            print("Valor inválido para el parámetro ss")

    def validar_dia(self, dia):
        try:
            dia = int(dia)
            return 1 <= dia <= 31
        except ValueError:
            return False

    def validar_mes(self, mes):
        try:
            mes = int(mes)
            return 1 <= mes <= 12
        except ValueError:
            return False

    def validar_anio(self, anio):
        try:
            anio = int(anio)
            return anio >= 0
        except ValueError:
            return False

    def validar_hora(self, hora):
        try:
            hora = int(hora)
            return 0 <= hora <= 23
        except ValueError:
            return False

    def validar_minuto(self, minuto):
        try:
            minuto = int(minuto)
            return 0 <= minuto <= 59
        except ValueError:
            return False

    def validar_segundo(self, segundo):
        try:
            segundo = int(segundo)
            return 0 <= segundo <= 59
        except ValueError:
            return False

    def __str__(self):
        return self.fecha +" "+ self.hora


# Ejemplo de uso
fecha_hora = FechaHora()

# Fijar la fecha
fecha_hora.fijarFecha("2015-09-30")

# Fijar la hora
fecha_hora.fijarHora("17:45:00")

# Mostrar la fecha y hora inicial
print(fecha_hora)  # Resultado: 2015/09/30 17:45:00

# Cambiar el mes
fecha_hora.cambiar("mm=10")

# Mostrar la fecha y hora después de cambiar el mes
print(fecha_hora)  # Resultado: 2015/10/30 17:45:00

# Fijar la hora y cambiar el año
fecha_hora.fijarHora("18:00:00")
fecha_hora.cambiar("aaaa=2016")

# Mostrar la fecha y hora final
print(fecha_hora)  # Resultado: 2016/10/30 18:00:00
