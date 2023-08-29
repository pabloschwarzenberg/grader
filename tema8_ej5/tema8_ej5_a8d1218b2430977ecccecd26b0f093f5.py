class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        return f"{self.fecha} {self.hora}"

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        parametro, valor = parte.split("=")
        parametro = parametro.strip().lower()
        valor = valor.strip()

        if parametro in ["dd", "mm", "aaaa", "hh", "mi", "ss"]:
            setattr(self, parametro, valor)
        else:
            print("Error: Parámetro no válido.")
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
