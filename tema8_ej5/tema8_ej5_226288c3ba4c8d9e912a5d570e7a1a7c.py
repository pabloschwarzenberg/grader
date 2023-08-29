class FechaHora:
    def __init__(self):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minuto = None
        self.segundo = None

    def __str__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        if len(partes) != 3:
            partes = fecha.split("-")
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(":")
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        parametro, valor = parte.split("=")
        parametro = parametro.strip()
        valor = valor.strip()
        
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
            if anio >= 0:
                self.anio = anio
            else:
                print("Año inválido.")
        elif parametro == "HH":
            hora = int(valor)
            if hora >= 0 and hora <= 23:
                self.hora = hora
            else:
                print("Hora inválida.")
        elif parametro == "MM":
            minuto = int(valor)
            if minuto >= 0 and minuto <= 59:
                self.minuto = minuto
            else:
                print("Minuto inválido.")
        elif parametro == "SS":
            segundo = int(valor)
            if segundo >= 0 and segundo <= 59:
                self.segundo = segundo
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
           