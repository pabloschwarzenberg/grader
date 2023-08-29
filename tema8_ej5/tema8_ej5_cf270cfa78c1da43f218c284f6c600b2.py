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
        fecha, hora = fechahora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        parametro, valor = parte.split('=')
        parametro = parametro.strip()
        valor = valor.strip()

        if parametro == 'dd':
            if 1 <= int(valor) <= 31:
                self.fecha = self.fecha[:3] + valor + self.fecha[5:]
            else:
                print("Error: Día inválido")
        elif parametro == 'mm':
            if 1 <= int(valor) <= 12:
                self.fecha = self.fecha[:0] + valor + self.fecha[2:]
            else:
                print("Error: Mes inválido")
        elif parametro == 'aaaa':
            self.fecha = valor + self.fecha[4:]
        elif parametro == 'HH':
            if 0 <= int(valor) <= 23:
                self.hora = valor + self.hora[2:]
            else:
                print("Error: Hora inválida")
        elif parametro == 'MM':
            if 0 <= int(valor) <= 59:
                self.hora = self.hora[:0] + valor + self.hora[2:]
            else:
                print("Error: Minuto inválido")
        elif parametro == 'SS':
            if 0 <= int(valor) <= 59:
                self.hora = self.hora[:3] + valor
            else:
                print("Error: Segundo inválido")
        else:
            print("Error: Parámetro no reconocido")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
