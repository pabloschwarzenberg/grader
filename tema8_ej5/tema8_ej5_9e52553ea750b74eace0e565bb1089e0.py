class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.fecha[2], self.fecha[1], self.fecha[0], self.hora[0], self.hora[1], self.hora[2])

    def fijarFecha(self, fecha):
        if "/" in fecha:
            self.fecha = list(map(int, fecha.split("/")))
        elif "-" in fecha:
            self.fecha = list(map(int, fecha.split("-")))

    def fijarHora(self, hora):
        self.hora = list(map(int, hora.split(":")))

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        parte = parte.replace(" ", "")
        tipo, valor = parte.split("=")

        if tipo == "dd":
            if int(valor) < 1 or int(valor) > 31:
                print("Error: El día debe estar entre 1 y 31.")
            else:
                self.fecha[0] = int(valor)
        elif tipo == "mm":
            if int(valor) < 1 or int(valor) > 12:
                print("Error: El mes debe estar entre 1 y 12.")
            else:
                self.fecha[1] = int(valor)
        elif tipo == "aaaa":
            self.fecha[2] = int(valor)
        elif tipo == "HH":
            if int(valor) < 0 or int(valor) > 23:
                print("Error: La hora debe estar entre 0 y 23.")
            else:
                self.hora[0] = int(valor)
        elif tipo == "MM":
            if int(valor) < 0 or int(valor) > 59:
                print("Error: Los minutos deben estar entre 0 y 59.")
            else:
                self.hora[1] = int(valor)
        elif tipo == "SS":
            if int(valor) < 0 or int(valor) > 59:
                print("Error: Los segundos deben estar entre 0 y 59.")
            else:
                self.hora[2] = int(valor)
        else:
            print("Error: Tipo de parámetro inválido.")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
