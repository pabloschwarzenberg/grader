class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return ""
    
    def fijarFecha(self,fecha):
        pass

    def fijarHora(self,hora):
        pass
      
    def fijarFechaHora(self,fechahora):
        pass

    def cambiar(self,parte):
        pass

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        fecha_str = self.fecha.strftime("%Y/%m/%d")
        hora_str = self.hora.strftime("%H:%M:%S")
        return f"{fecha_str} {hora_str}"

    def fijarFecha(self, fecha):
        try:
            from datetime import datetime
            self.fecha = datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            print("Error: formato de fecha inválido. Utilice dd/mm/aaaa")

    def fijarHora(self, hora):
        try:
            from datetime import datetime
            self.hora = datetime.strptime(hora, "%H:%M:%S")
        except ValueError:
            print("Error: formato de hora inválido. Utilice HH:MM:SS")

    def fijarFechaHora(self, fechahora):
        try:
            from datetime import datetime
            self.fecha, self.hora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            print("Error: formato de fecha y hora inválido. Utilice dd/mm/aaaa HH:MM:SS")

    def cambiar(self, parte):
        try:
            import re
            match = re.match(r"(\w+)\s*=\s*(\w+)", parte)
            if match:
                parte, valor = match.groups()
                if parte == "dd":
                    self.fecha = self.fecha.replace(day=int(valor))
                elif parte == "mm":
                    self.fecha = self.fecha.replace(month=int(valor))
                elif parte == "aaaa":
                    self.fecha = self.fecha.replace(year=int(valor))
                elif parte == "HH":
                    self.hora = self.hora.replace(hour=int(valor))
                elif parte == "MM":
                    self.hora = self.hora.replace(minute=int(valor))
                elif parte == "SS":
                    self.hora = self.hora.replace(second=int(valor))
                else:
                    print("Error: parámetro inválido.")
            else:
                print("Error: formato de cambio inválido.")
        except ValueError:
            print("Error: valor inválido para el parámetro.")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
