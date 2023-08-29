class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None
        
    def __str__(self):
        fecha_str = "{:%Y/%m/%d}".format(self.fecha)
        hora_str = "{:%H:%M:%S}".format(self.hora)
        return "{} {}".format(fecha_str, hora_str)

    def fijarFecha(self, fecha):
        from datetime import datetime
        formato = "%d/%m/%Y" if "/" in fecha else "%d-%m-%Y"
        try:
            self.fecha = datetime.strptime(fecha, formato).date()
        except ValueError:
            print("Fecha inválida")

    def fijarHora(self, hora):
        from datetime import datetime
        try:
            self.hora = datetime.strptime(hora, "%H:%M:%S").time()
        except ValueError:
            print("Hora inválida")

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split(" ")
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        partes = parte.split("=")
        tipo = partes[0].strip()
        valor = partes[1].strip()

        if tipo == "dd":
            self.cambiar_dia(int(valor))
        elif tipo == "mm":
            self.cambiar_mes(int(valor))
        elif tipo == "aaaa":
            self.cambiar_anio(int(valor))
        elif tipo == "HH":
            self.cambiar_hora(int(valor))
        elif tipo == "MM":
            self.cambiar_minuto(int(valor))
        elif tipo == "SS":
            self.cambiar_segundo(int(valor))
        else:
            print("Parámetro inválido")

    def cambiar_dia(self, dia):
        if not self.fecha:
            print("La fecha no ha sido fijada")
            return

        try:
            self.fecha = self.fecha.replace(day=dia)
        except ValueError:
            print("Día inválido")

    def cambiar_mes(self, mes):
        if not self.fecha:
            print("La fecha no ha sido fijada")
            return

        try:
            self.fecha = self.fecha.replace(month=mes)
        except ValueError:
            print("Mes inválido")

    def cambiar_anio(self, anio):
        if not self.fecha:
            print("La fecha no ha sido fijada")
            return

        try:
            self.fecha = self.fecha.replace(year=anio)
        except ValueError:
            print("Año inválido")

    def cambiar_hora(self, hora):
        if not self.hora:
            print("La hora no ha sido fijada")
            return

        try:
            self.hora = self.hora.replace(hour=hora)
        except ValueError:
            print("Hora inválida")

    def cambiar_minuto(self, minuto):
        if not self.hora:
            print("La hora no ha sido fijada")
            return

        try:
            self.hora = self.hora.replace(minute=minuto)
        except ValueError:
            print("Minuto inválido")

    def cambiar_segundo(self, segundo):
        if not self.hora:
            print("La hora no ha sido fijada")
            return

        try:
            self.hora = self.hora.replace(second=segundo)
        except ValueError:
            print("Segundo inválido")


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
