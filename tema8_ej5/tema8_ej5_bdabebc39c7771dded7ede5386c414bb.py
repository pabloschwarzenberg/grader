class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        return f"{self.fecha} {self.hora}"

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        partes = parte.split("=")
        if len(partes) == 2:
            parametro = partes[0].strip()
            valor = partes[1].strip()

            if parametro == "dd":
                if valor.isnumeric():
                    dia = int(valor)
                    if dia >= 1 and dia <= 31:
                        self.fecha = self.fecha[:2] + valor + self.fecha[2:]
                    else:
                        print("Día inválido.")
                else:
                    print("Día inválido.")

            elif parametro == "mm":
                if valor.isnumeric():
                    mes = int(valor)
                    if mes >= 1 and mes <= 12:
                        self.fecha = self.fecha[:5] + valor + self.fecha[5:]
                    else:
                        print("Mes inválido.")
                else:
                    print("Mes inválido.")

            elif parametro == "aaaa":
                if valor.isnumeric():
                    self.fecha = valor + self.fecha[4:]
                else:
                    print("Año inválido.")

            elif parametro == "HH":
                if valor.isnumeric():
                    hora = int(valor)
                    if hora >= 0 and hora <= 23:
                        self.hora = valor + self.hora[2:]
                    else:
                        print("Hora inválida.")
                else:
                    print("Hora inválida.")

            elif parametro == "MM":
                if valor.isnumeric():
                    minuto = int(valor)
                    if minuto >= 0 and minuto <= 59:
                        self.hora = self.hora[:3] + valor + self.hora[5:]
                    else:
                        print("Minuto inválido.")
                else:
                    print("Minuto inválido.")

            elif parametro == "SS":
                if valor.isnumeric():
                    segundo = int(valor)
                    if segundo >= 0 and segundo <= 59:
                        self.hora = self.hora[:6] + valor
                    else:
                        print("Segundo inválido.")
                else:
                    print("Segundo inválido.")

            else:
                print("Parámetro inválido.")
        else:
            print("Formato de parámetro incorrecto.")


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
