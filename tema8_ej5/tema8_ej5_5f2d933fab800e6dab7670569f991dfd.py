import datetime

class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        fecha_str = self.fecha.strftime("%Y/%m/%d") if self.fecha else ""
        hora_str = self.hora.strftime("%H:%M:%S") if self.hora else ""
        return "{} {}".format(fecha_str, hora_str)

    def fijarFecha(self, fecha):
        try:
            self.fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        except ValueError:
            print("Formato de fecha incorrecto. Utilice el formato dd/mm/aaaa")

    def fijarHora(self, hora):
        try:
            self.hora = datetime.datetime.strptime(hora, "%H:%M:%S").time()
        except ValueError:
            print("Formato de hora incorrecto. Utilice el formato HH:MM:SS")

    def fijarFechaHora(self, fechahora):
        try:
            self.fecha = datetime.datetime.strptime(fechahora, "%d-%m-%Y %H:%M:%S").date()
            self.hora = datetime.datetime.strptime(fechahora, "%d-%m-%Y %H:%M:%S").time()
        except ValueError:
            print("Formato de fecha y hora incorrecto. Utilice el formato dd-mm-aaaa HH:MM:SS")

    def cambiar(self, parte):
        partes = parte.split("=")
        if len(partes) == 2:
            tipo = partes[0].strip()
            valor = partes[1].strip()

            if tipo == "dd":
                if 1 <= int(valor) <= 31:
                    self.fecha = self.fecha.replace(day=int(valor))
                else:
                    print("Día inválido. El rango válido es de 1 a 31.")

            elif tipo == "mm":
                if 1 <= int(valor) <= 12:
                    self.fecha = self.fecha.replace(month=int(valor))
                else:
                    print("Mes inválido. El rango válido es de 1 a 12.")

            elif tipo == "aaaa":
                if int(valor) >= 0:
                    self.fecha = self.fecha.replace(year=int(valor))
                else:
                    print("Año inválido. El valor debe ser mayor o igual a 0.")

            elif tipo == "HH":
                if 0 <= int(valor) <= 23:
                    self.hora = self.hora.replace(hour=int(valor))
                else:
                    print("Hora inválida. El rango válido es de 0 a 23.")

            elif tipo == "MM":
                if 0 <= int(valor) <= 59:
                    self.hora = self.hora.replace(minute=int(valor))
                else:
                    print("Minuto inválido. El rango válido es de 0 a 59.")

            elif tipo == "SS":
                if 0 <= int(valor) <= 59:
                    self.hora = self.hora.replace(second=int(valor))
                else:
                    print("Segundo inválido. El rango válido es de 0 a 59.")

            else:
                print("Tipo de parámetro inválido.")

        else:
            print("Formato de parámetro incorrecto. Utilice el formato 'tipo = valor'")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
