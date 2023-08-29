class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def __str__(self):
        return "{self.fecha} {self.hora}"

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split()
        fecha = partes[0]
        hora = partes[1]
        self.fecha = self.convertirFormatoFecha(fecha)
        self.hora = self.convertirFormatoHora(hora)

    def cambiar(self, parte):
        parametro, valor = parte.split("=")
        parametro = parametro.strip()
        valor = valor.strip()

        if parametro == "dd":
            if int(valor) > 0 and int(valor) <= 31:
                self.fecha = self.fecha[:8] + valor + self.fecha[10:]
            else:
                print("Error: Día inválido.")
        elif parametro == "mm":
            if int(valor) > 0 and int(valor) <= 12:
                self.fecha = self.fecha[:5] + valor + self.fecha[7:]
            else:
                print("Error: Mes inválido.")
        elif parametro == "aaaa":
            self.fecha = self.fecha[:2] + valor + self.fecha[4:]
        elif parametro == "HH":
            if int(valor) >= 0 and int(valor) < 24:
                self.hora = self.hora[:3] + valor + self.hora[5:]
            else:
                print("Error: Hora inválida.")
        elif parametro == "MM":
            if int(valor) >= 0 and int(valor) < 60:
                self.hora = self.hora[:6] + valor + self.hora[8:]
            else:
                print("Error: Minutos inválidos.")
        elif parametro == "SS":
            if int(valor) >= 0 and int(valor) < 60:
                self.hora = self.hora[:9] + valor
            else:
                print("Error: Segundos inválidos.")
        else:
            print("Error: Parámetro inválido.")

    def convertirFormatoFecha(self, fecha):
        partes = fecha.split("-")
        return "{partes[2]}/{partes[1]}/{partes[0]}"

    def convertirFormatoHora(self, hora):
        return hora

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
