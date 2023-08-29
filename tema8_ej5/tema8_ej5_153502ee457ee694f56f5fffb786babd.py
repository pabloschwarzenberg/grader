class FechaHora:
    def __init__(self):
        self.fecha = ["0", "1", "2"]
        self.hora = ["0", "0", "0"]

    def __str__(self):
        self.fecha.reverse()
        fecha = self.fecha
        fecha = "/".join(fecha)
        hora = ":".join(self.hora)
        self.fecha.reverse()
        fechahora = fecha+" "+hora
        return fechahora

    def fijarFecha(self, fecha):
        for i in fecha:
            if i == "-":
                fecha = fecha.split("-")
                break
            if i == "/":
                fecha = fecha.split("/")
                break
        for i in range(len(fecha)):
            self.fecha[i] = fecha[i]

    def fijarHora(self, hora):
        hora = hora.split(":")
        for i in range(len(hora)):
            self.hora[i] = hora[i]

    def fijarFechaHora(self, fechahora):
        fechahora = fechahora.split(" ")
        for i in range(len(fechahora)):
            for j in fechahora[i]:
                fechaohora = fechahora[i]
                if j == '-':
                    fechahora[i] = fechaohora.split("-")
                    break
                if j == "/":
                    fechahora[i] = fechaohora.split("/")
                    break
                if j == ":":
                    fechahora[i] = fechaohora.split(":")
                    break
        print(fechahora)
        for i in range(1):
            for j in range(len(fechahora[i])):
                print(fechahora[i][j])
                self.fecha[j] = fechahora[i][j]
            for j in range(len(fechahora[i+1])):
                print(fechahora[i+1][j])
                self.hora[j] = fechahora[i+1][j]

    def cambiar(self, parte):
        parte = parte.replace(" ", "")
        parte = parte.split("=")
        if parte[0] == "aaaa":
            self.fecha[2] = parte[1]
        elif parte[0] == "mm":
            self.fecha[1] = parte[1]
        elif parte[0] == "dd":
            self.fecha[0] = parte[1]
        elif parte[0] == "HH":
            self.hora[2] = parte[1]
        elif parte[0] == "MM":
            self.hora[1] = parte[1]
        elif parte[0] == "SS":
            self.hora[0] = parte[1]


if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           