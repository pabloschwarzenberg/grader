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
        self.dia = None
        self.mes = None
        self.anno = None
        self.hora = None
        self.minuto = None
        self.segundo = None

    def __str__(self):
        fecha = f"{self.anno:04d}/{self.mes:02d}/{self.dia:02d}"
        hora = f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
        return f"{fecha} {hora}"

    def fijarFecha(self, fecha):
        self.dia, self.mes, self.anno = map(int, fecha.split("/"))

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(":"))

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        parametro, valor = map(str.strip, parte.split("="))

        if parametro == "dd":
            if valor.isdigit():
                dia = int(valor)
                if 1 <= dia <= 31:
                    self.dia = dia
                else:
                    print("Valor de día inválido")
            else:
                print("Valor de día inválido")

        elif parametro == "mm":
            if valor.isdigit():
                mes = int(valor)
                if 1 <= mes <= 12:
                    self.mes = mes
                else:
                    print("Valor de mes inválido")
            else:
                print("Valor de mes inválido")

        elif parametro == "aaaa":
            if valor.isdigit():
                anno = int(valor)
                if anno > 0:
                    self.anno = anno
                else:
                    print("Valor de año inválido")
            else:
                print("Valor de año inválido")

        elif parametro == "HH":
            if valor.isdigit():
                hora = int(valor)
                if 0 <= hora <= 23:
                    self.hora = hora
                else:
                    print("Valor de hora inválido")
            else:
                print("Valor de hora inválido")

        elif parametro == "MM":
            if valor.isdigit():
                minuto = int(valor)
                if 0 <= minuto <= 59:
                    self.minuto = minuto
                else:
                    print("Valor de minuto inválido")
            else:
                print("Valor de minuto inválido")

        elif parametro == "SS":
            if valor.isdigit():
                segundo = int(valor)
                if 0 <= segundo <= 59:
                    self.segundo = segundo
                else:
                    print("Valor de segundo inválido")
            else:
                print("Valor de segundo inválido")

        else:
            print("Parámetro inválido")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")