class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def __str__(self):
        return f"{self.fecha} {self.hora}"

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split(" ")
        self.fecha = partes[0]
        self.hora = partes[1]

    def cambiar(self, parte):
        partes = parte.split("=")
        tipo = partes[0].strip()
        valor = partes[1].strip()

        if tipo == "dd":
            dia = int(valor)
            if dia > 0 and dia <= 31:
                self.fecha = self.fecha[:3] + valor + self.fecha[5:]
            else:
                print("Día inválido.")
        elif tipo == "mm":
            mes = int(valor)
            if mes > 0 and mes <= 12:
                self.fecha = self.fecha[:0] + valor + self.fecha[2:]
            else:
                print("Mes inválido.")
        elif tipo == "aaaa":
            self.fecha = valor + self.fecha[4:]
        elif tipo == "HH":
            hora = int(valor)
            if hora >= 0 and hora < 24:
                self.hora = valor + self.hora[2:]
            else:
                print("Hora inválida.")
        elif tipo == "MM":
            minuto = int(valor)
            if minuto >= 0 and minuto < 60:
                self.hora = self.hora[:0] + valor + self.hora[2:]
            else:
                print("Minuto inválido.")
        elif tipo == "SS":
            segundo = int(valor)
            if segundo >= 0 and segundo < 60:
                self.hora = self.hora[:3] + valor
            else:
                print("Segundo inválido.")
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

           