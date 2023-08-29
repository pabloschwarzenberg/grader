class FechaHora:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.anio = 0
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return "{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(":")
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split(" ")
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        parametro, valor = parte.strip().split("=")

        if parametro == "dd":
            nuevo_dia = int(valor)
            if nuevo_dia >= 1 and nuevo_dia <= 31:
                self.dia = nuevo_dia
            else:
                print("Día inválido.")
        elif parametro == "mm":
            nuevo_mes = int(valor)
            if nuevo_mes >= 1 and nuevo_mes <= 12:
                self.mes = nuevo_mes
            else:
                print("Mes inválido.")
        elif parametro == "aaaa":
            nuevo_anio = int(valor)
            if nuevo_anio >= 0:
                self.anio = nuevo_anio
            else:
                print("Año inválido.")
        elif parametro == "HH":
            nueva_hora = int(valor)
            if nueva_hora >= 0 and nueva_hora <= 23:
                self.hora = nueva_hora
            else:
                print("Hora inválida.")
        elif parametro == "MM":
            nuevo_minuto = int(valor)
            if nuevo_minuto >= 0 and nuevo_minuto <= 59:
                self.minuto = nuevo_minuto
            else:
                print("Minuto inválido.")
        elif parametro == "SS":
            nuevo_segundo = int(valor)
            if nuevo_segundo >= 0 and nuevo_segundo <= 59:
                self.segundo = nuevo_segundo
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
