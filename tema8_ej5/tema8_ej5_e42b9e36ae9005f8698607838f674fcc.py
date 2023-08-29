class FechaHora:
    def __init__(self):
        self.aaaa = '1970'
        self.mes = '01'
        self.dia = '01'
        self.hora = '00'
        self.minutos = '00'
        self.segundos = '00'

    def __str__(self):
        return self.aaaa + '/' + self.mes + '/' + self.dia + ' ' + self.hora + ':' + self.minutos + ':' + self.segundos

    def fijarFecha(self, fecha):
        self.dia = fecha[0:2]
        self.mes = fecha[3:5]
        self.aaaa = fecha[6:10]

    def fijarHora(self, hora):
        self.hora = hora[0:2]
        self.minutos = hora[3:5]
        self.segundos = hora[6:8]

    def fijarFechaHora(self, fechahora):
        self.dia = fechahora[0:2]
        self.mes = fechahora[3:5]
        self.aaaa = fechahora[6:10]
        self.hora = fechahora[11:13]
        self.minutos = fechahora[14:16]
        self.segundos = fechahora[17:19]

    def cambiar(self, parte):
        parte = parte.replace(' ', '')
        datos = parte.split('=')
        medida = datos[0]
        valor = datos[1]
        if len(valor) == 0:
            valor = '00'
        elif len(valor) == 1:
            valor = '0' + valor
        if medida == 'aaaa':
            self.aaaa = valor
        elif medida == 'mm':
            if int(valor) > 12:
                print('¡Ándate a inventar fechas a otro lado!')
            self.mes = valor
        elif medida == 'dd':
            if int(valor) > 31:
                print('¡Ándate a inventar fechas a otro lado!')
            self.dia = valor
        elif medida == 'HH':
            if int(valor) > 24:
                print('¡Ándate a inventar fechas a otro lado!')
            self.hora = valor
        elif medida == 'MM':
            if int(valor) > 60:
                print('¡Ándate a inventar fechas a otro lado!')
            self.minutos = valor
        elif medida == 'SS':
            if int(valor) > 60:
                print('¡Ándate a inventar fechas a otro lado!')
            self.segundos = valor


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
