class FechaHora:
    def __init__(self):
        self.dia = None
        self.mes = None
        self.anno = None
        self.hora = None
        self.minuto = None
        self.segundo = None

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        if len(partes) != 3:
            partes = fecha.split("-")

        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anno = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(":")
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(" ")
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parametro):
        partes = parametro.split("=")
        tipo_parametro = partes[0].strip()
        valor = partes[1].strip()

        if tipo_parametro == "dd":
            dia = int(valor)
            if dia < 1 or dia > 31:
                print("Error: Valor inválido para día.")
                return
            self.dia = dia

        elif tipo_parametro == "mm":
            mes = int(valor)
            if mes < 1 or mes > 12:
                print("Error: Valor inválido para mes.")
                return
            self.mes = mes

        elif tipo_parametro == "aaaa":
            anno = int(valor)
            if anno < 0:
                print("Error: Valor inválido para año.")
                return
            self.anno = anno

        elif tipo_parametro == "HH":
            hora = int(valor)
            if hora < 0 or hora > 23:
                print("Error: Valor inválido para hora.")
                return
            self.hora = hora

        elif tipo_parametro == "MM":
            minuto = int(valor)
            if minuto < 0 or minuto > 59:
                print("Error: Valor inválido para minuto.")
                return
            self.minuto = minuto

        elif tipo_parametro == "SS":
            segundo = int(valor)
            if segundo < 0 or segundo > 59:
                print("Error: Valor inválido para segundo.")
                return
            self.segundo = segundo

        else:
            print("Error: Parámetro inválido.")

    def __str__(self):
        return f"{self.anno}/{self.mes}/{self.dia} {self.hora}:{self.minuto}:{self.segundo}"


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("01/01/2023")
    fecha_hora.fijarHora("12:30:45")
    fecha_hora.cambiar("dd=2")
    fecha_hora.cambiar("mm=4")
    fecha_hora.cambiar("HH=9")
    fecha_hora.cambiar("MM=15")
    fecha_hora.cambiar("SS=0")
    print(fecha_hora)         