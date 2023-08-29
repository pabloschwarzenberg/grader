class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        fecha_str = self.fecha.strftime("%Y/%m/%d")
        hora_str = self.hora.strftime("%H:%M:%S")
        return "{} {}".format(fecha_str, hora_str)

    def fijarFecha(self, fecha):
        from datetime import datetime
        self.fecha = datetime.strptime(fecha, "%d/%m/%Y")

    def fijarHora(self, hora):
        from datetime import datetime
        self.hora = datetime.strptime(hora, "%H:%M:%S")

    def fijarFechaHora(self, fechahora):
        from datetime import datetime
        self.fecha, self.hora = datetime.strptime(fechahora, "%d-%m-%Y %H:%M:%S").date(), datetime.strptime(fechahora, "%d-%m-%Y %H:%M:%S").time()

    def cambiar(self, parte):
        partes = parte.split("=")
        parametro = partes[0].strip()
        valor = partes[1].strip()
        if parametro == "dd":
            self.validar_dia(valor)
            self.fecha = self.fecha.replace(day=int(valor))
        elif parametro == "mm":
            self.validar_mes(valor)
            self.fecha = self.fecha.replace(month=int(valor))
        elif parametro == "aaaa":
            self.validar_anio(valor)
            self.fecha = self.fecha.replace(year=int(valor))
        elif parametro == "HH":
            self.validar_hora(valor)
            self.hora = self.hora.replace(hour=int(valor))
        elif parametro == "MM":
            self.validar_minuto(valor)
            self.hora = self.hora.replace(minute=int(valor))
        elif parametro == "SS":
            self.validar_segundo(valor)
            self.hora = self.hora.replace(second=int(valor))

    def validar_dia(self, dia):
        dia = int(dia)
        if dia < 1 or dia > 31:
            print("Día inválido. Debe ser un valor entre 1 y 31.")

    def validar_mes(self, mes):
        mes = int(mes)
        if mes < 1 or mes > 12:
            print("Mes inválido. Debe ser un valor entre 1 y 12.")

    def validar_anio(self, anio):
        anio = int(anio)
        if anio < 1:
            print("Año inválido. Debe ser un valor mayor a 0.")

    def validar_hora(self, hora):
        hora = int(hora)
        if hora < 0 or hora > 23:
            print("Hora inválida. Debe ser un valor entre 0 y 23.")

    def validar_minuto(self, minuto):
        minuto = int(minuto)
        if minuto < 0 or minuto > 59:
            print("Minuto inválido. Debe ser un valor entre 0 y 59.")

    def validar_segundo(self, segundo):
        segundo = int(segundo)
        if segundo < 0 or segundo > 59:
            print("Segundo inválido. Debe ser un valor entre 0 y 59.")


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           