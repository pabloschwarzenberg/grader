class FechaHora:
    def __init__(self):
        self.fecha = [1, 1, 1900]
        self.hora = [0, 0, 0]

    def fijarFecha(self, fecha_str):
        fecha_str = fecha_str.replace("-", "/")
        dia, mes, anio = map(int, fecha_str.split("/"))
        self.fecha = [dia, mes, anio]

    def fijarHora(self, hora_str):
        hora, minuto, segundo = map(int, hora_str.split(":"))
        self.hora = [hora, minuto, segundo]

    def fijarFechaHora(self, fechahora_str):
        fecha_str, hora_str = fechahora_str.split()
        self.fijarFecha(fecha_str)
        self.fijarHora(hora_str)

    def cambiar(self, parametro_str):
        parametro_str = parametro_str.replace(" ", "")
        parametro, valor = parametro_str.split("=")
        valor = int(valor)

        if parametro == "dd":
            if 1 <= valor <= 31:
                self.fecha[0] = valor
            else:
                print("Valor de día inválido")
        elif parametro == "mm":
            if 1 <= valor <= 12:
                self.fecha[1] = valor
            else:
                print("Valor de mes inválido")
        elif parametro == "aaaa":
            if valor >= 1900:
                self.fecha[2] = valor
            else:
                print("Valor de año inválido")
        elif parametro == "HH":
            if 0 <= valor <= 23:
                self.hora[0] = valor
            else:
                print("Valor de hora inválido")
        elif parametro == "MM":
            if 0 <= valor <= 59:
                self.hora[1] = valor
            else:
                print("Valor de minuto inválido")
        elif parametro == "SS":
            if 0 <= valor <= 59:
                self.hora[2] = valor
            else:
                print("Valor de segundo inválido")

    def __str__(self):
        dia, mes, anio = self.fecha
        hora, minuto, segundo = self.hora
        return anio:04d, "/",mes:02d, "/",dia:02d  hora:02d,":",minuto:02d, ":",segundo:02d
fechahora = FechaHora()
fechahora.fijarFecha("01/01/2000")
fechahora.fijarHora("12:00:00")
fechahora.cambiar("dd=2")
print(fechahora)
