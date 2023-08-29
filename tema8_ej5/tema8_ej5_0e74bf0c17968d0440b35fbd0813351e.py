class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.fecha[6:], self.fecha[3:5], self.fecha[:2],
                                          self.hora[:2], self.hora[3:5], self.hora[6:])

    def fijarFecha(self, fecha):
        self.fecha = fecha.replace("-", "/")

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        tipo, valor = parte.split('=')

        if tipo.strip() == 'dd':
            dia = int(valor.strip())
            if 1 <= dia <= 31:
                self.fecha = "{:02d}{}".format(dia, self.fecha[2:])
            else:
                print("Día inválido.")
        elif tipo.strip() == 'mm':
            mes = int(valor.strip())
            if 1 <= mes <= 12:
                self.fecha = "{}{:02d}{}".format(self.fecha[:3], mes, self.fecha[5:])
            else:
                print("Mes inválido.")
        elif tipo.strip() == 'aaaa':
            anio = int(valor.strip())
            self.fecha = "{}{:04d}".format(self.fecha[:6], anio)
        elif tipo.strip() == 'HH':
            hora = int(valor.strip())
            if 0 <= hora <= 23:
                self.hora = "{:02d}{}".format(hora, self.hora[2:])
            else:
                print("Hora inválida.")
        elif tipo.strip() == 'MM':
            minuto = int(valor.strip())
            if 0 <= minuto <= 59:
                self.hora = "{}{:02d}{}".format(self.hora[:3], minuto, self.hora[5:])
            else:
                print("Minuto inválido.")
        elif tipo.strip() == 'SS':
            segundo = int(valor.strip())
            if 0 <= segundo <= 59:
                self.hora = "{}{:02d}".format(self.hora[:6], segundo)
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
