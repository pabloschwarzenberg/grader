class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )

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
        partes = fechahora.split(" ")
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        parametros = parte.split("=")
        parametro = parametros[0].strip()
        valor = parametros[1].strip()

        if parametro == "dd":
            if valor.isdigit():
                dia = int(valor)
                if dia >= 1 and dia <= 31:
                    self.dia = dia
                else:
                    print("Día inválido.")
            else:
                print("Valor de día inválido.")

        elif parametro == "mm":
            if valor.isdigit():
                mes = int(valor)
                if mes >= 1 and mes <= 12:
                    self.mes = mes
                else:
                    print("Mes inválido.")
            else:
                print("Valor de mes inválido.")

        elif parametro == "aaaa":
            if valor.isdigit():
                anio = int(valor)
                if anio >= 1:
                    self.anio = anio
                else:
                    print("Año inválido.")
            else:
                print("Valor de año inválido.")

        elif parametro == "HH":
            if valor.isdigit():
                hora = int(valor)
                if hora >= 0 and hora <= 23:
                    self.hora = hora
                else:
                    print("Hora inválida.")
            else:
                print("Valor de hora inválido.")

        elif parametro == "MM":
            if valor.isdigit():
                minuto = int(valor)
                if minuto >= 0 and minuto <= 59:
                    self.minuto = minuto
                else:
                    print("Minuto inválido.")
            else:
                print("Valor de minuto inválido.")

        elif parametro == "SS":
            if valor.isdigit():
                segundo = int(valor)
                if segundo >= 0 and segundo <= 59:
                    self.segundo = segundo
                else:
                    print("Segundo inválido.")
            else:
                print("Valor de segundo inválido.")

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
