class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def __str__(self):
        return f"{self.fecha} {self.hora}"

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        self.fecha, self.hora = fechahora.split(' ')

    def cambiar(self, parte):
        clave, valor = parte.split('=')
        clave = clave.strip()  # Eliminar espacios en blanco alrededor de la clave
        valor = valor.strip()  # Eliminar espacios en blanco alrededor del valor

        if clave == 'dd':
            self.fecha = valor + self.fecha[2:]
        elif clave == 'mm':
            self.fecha = self.fecha[:3] + valor + self.fecha[5:]
        elif clave == 'aaaa':
            self.fecha = valor + self.fecha[4:]
        elif clave == 'HH':
            self.hora = valor + self.hora[2:]
        elif clave == 'MM':
            self.hora = self.hora[:3] + valor + self.hora[5:]
        elif clave == 'SS':
            self.hora = self.hora[:6] + valor
        else:
            print("Error: Parámetro inválido")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
