class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        return {self.fecha}, {self.hora}

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        parte = parte.strip().lower()
        if parte.startswith("dd="):
            dia = int(parte.split("=")[1])
            if 1 <= dia <= 31:
                self.fecha = self.fecha[:2] + str(dia).zfill(2) + self.fecha[4:]
            else:
                print("Error: El día especificado es inválido.")
        elif parte.startswith("mm="):
            mes = int(parte.split("=")[1])
            if 1 <= mes <= 12:
                self.fecha = self.fecha[:3] + str(mes).zfill(2) + self.fecha[5:]
            else:
                print("Error: El mes especificado es inválido.")
        elif parte.startswith("aaaa="):
            anio = int(parte.split("=")[1])
            if anio >= 0:
                self.fecha = str(anio) + self.fecha[4:]
            else:
                print("Error: El año especificado es inválido.")
        elif parte.startswith("hh="):
            hora = int(parte.split("=")[1])
            if 0 <= hora < 24:
                self.hora = str(hora).zfill(2) + self.hora[2:]
            else:
                print("Error: La hora especificada es inválida.")
        elif parte.startswith("min="):
            minuto = int(parte.split("=")[1])
            if 0 <= minuto < 60:
                self.hora = self.hora[:3] + str(minuto).zfill(2) + self.hora[5:]
            else:
                print("Error: El minuto especificado es inválido.")
        elif parte.startswith("ss="):
            segundo = int(parte.split("=")[1])
            if 0 <= segundo < 60:
                self.hora = self.hora[:6] + str(segundo).zfill(2)
            else:
                print("Error: El segundo especificado es inválido.")
        else:
            print("Error: El formato del parámetro es inválido.")


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
