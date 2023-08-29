class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo)

    def fijarFecha(self, fecha):
        partes = fecha.split('-')
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(':')
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split(' ')
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        partes = parte.split('=')
        parametro = partes[0].strip()
        valor = int(partes[1].strip())

        if parametro == 'dd':
            if 1 <= valor <= 31:
                self.dia = valor
            else:
                print("Valor inválido para día.")
        elif parametro == 'mm':
            if 1 <= valor <= 12:
                self.mes = valor
            else:
                print("Valor inválido para mes.")
        elif parametro == 'aaaa':
            if valor >= 1:
                self.anio = valor
            else:
                print("Valor inválido para año.")
        elif parametro == 'HH':
            if 0 <= valor <= 23:
                self.hora = valor
            else:
                print("Valor inválido para hora.")
        elif parametro == 'MM':
            if 0 <= valor <= 59:
                self.minuto = valor
            else:
                print("Valor inválido para minuto.")
        elif parametro == 'SS':
            if 0 <= valor <= 59:
                self.segundo = valor
            else:
                print("Valor inválido para segundo.")
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