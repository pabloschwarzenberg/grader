class FechaHora:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.anio = 0
        self.hora = 0
        self.minutos = 0
        self.segundos = 0

    def __str__(self):
        fecha = "{:04d}/{:02d}/{:02d}".format(self.anio, self.mes, self.dia)
        hora = "{:02d}:{:02d}:{:02d}".format(self.hora, self.minutos, self.segundos)
        return fecha + " " + hora

    def fijarFecha(self, fecha):
        partes = fecha.replace("-", "/").split("/")
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(":")
        self.hora = int(partes[0])
        self.minutos = int(partes[1])
        self.segundos = int(partes[2])

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split(" ")
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        partes = parte.split("=")
        parametro = partes[0].strip()
        valor = partes[1].strip()

        if parametro == "dd":
            dia = int(valor)
            if dia >= 1 and dia <= 31:
                self.dia = dia
            else:
                print("Día inválido.")
        elif parametro == "mm":
            mes = int(valor)
            if mes >= 1 and mes <= 12:
                self.mes = mes
            else:
                print("Mes inválido.")
        elif parametro == "aaaa":
            anio = int(valor)
            self.anio = anio
        elif parametro == "HH":
            hora = int(valor)
            if hora >= 0 and hora <= 23:
                self.hora = hora
            else:
                print("Hora inválida.")
        elif parametro == "MM":
            minutos = int(valor)
            if minutos >= 0 and minutos <= 59:
                self.minutos = minutos
            else:
                print("Minutos inválidos.")
        elif parametro == "SS":
            segundos = int(valor)
            if segundos >= 0 and segundos <= 59:
                self.segundos = segundos
            else:
                print("Segundos inválidos.")
        else:
            print("Parámetro inválido.")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
