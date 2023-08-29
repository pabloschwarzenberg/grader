from datetime import datetime

class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def __str__(self):
        fecha_formateada = datetime.strptime(self.fecha, "%d-%m-%Y").strftime("%Y/%m/%d")
        return "{} {}".format(fecha_formateada, self.hora)

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fechahora = fechahora.split(" ")
        self.fecha = fechahora[0]
        self.hora = fechahora[1]

    def cambiar(self, parte):
        parametro, valor = parte.split("=")
        parametro = parametro.strip()
        valor = valor.strip()

        if parametro == "dd":
            if int(valor) <= 31:
                self.fecha = self.fecha.replace(self.fecha[:2], valor)
            else:
                print("Día inválido.")
        elif parametro == "mm":
            if int(valor) <= 12:
                self.fecha = self.fecha.replace(self.fecha[3:5], valor)
            else:
                print("Mes inválido.")
        elif parametro == "aaaa":
            self.fecha = self.fecha.replace(self.fecha[6:], valor)
        elif parametro == "HH":
            if int(valor) <= 23:
                self.hora = self.hora.replace(self.hora[:2], valor)
            else:
                print("Hora inválida.")
        elif parametro == "MM":
            if int(valor) <= 59:
                self.hora = self.hora.replace(self.hora[3:5], valor)
            else:
                print("Minuto inválido.")
        elif parametro == "SS":
            if int(valor) <= 59:
                self.hora = self.hora.replace(self.hora[6:], valor)
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
