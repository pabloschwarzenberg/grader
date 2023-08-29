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
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

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
        partes = fechahora.split()
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        clave, valor = parte.split("=")
        clave = clave.strip()
        valor = valor.strip()

        if clave == "dd":
            if 1 <= int(valor) <= 31:
                self.dia = int(valor)
            else:
                print("Error: Valor inválido para día.")
        elif clave == "mm":
            if 1 <= int(valor) <= 12:
                self.mes = int(valor)
            else:
                print("Error: Valor inválido para mes.")
        elif clave == "aaaa":
            if int(valor) >= 1900:
                self.anio = int(valor)
            else:
                print("Error: Valor inválido para año.")
        elif clave == "HH":
            if 0 <= int(valor) < 24:
                self.hora = int(valor)
            else:
                print("Error: Valor inválido para hora.")
        elif clave == "MM":
            if 0 <= int(valor) < 60:
                self.minuto = int(valor)
            else:
                print("Error: Valor inválido para minuto.")
        elif clave == "SS":
            if 0 <= int(valor) < 60:
                self.segundo = int(valor)
            else:
                print("Error: Valor inválido para segundo.")
        else:
            print("Error: Clave inválida.")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           