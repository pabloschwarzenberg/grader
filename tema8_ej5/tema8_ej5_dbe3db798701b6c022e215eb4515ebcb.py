class FechaHora:
    def __init__(self, dia, mes, anio, hora, minuto, segundo):
        self.dia = dia
        self.mes = mes
        self.anio = anio
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def fijarFecha(self, fecha):
        dia, mes, anio = fecha.split('/')
        self.dia = int(dia)
        self.mes = int(mes)
        self.anio = int(anio)

    def fijarHora(self, hora):
        hora, minuto, segundo = hora.split(':')
        self.hora = int(hora)
        self.minuto = int(minuto)
        self.segundo = int(segundo)

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        parametro = parametro.replace(' ', '')
        tipo, valor = parametro.split('=')
        valor = int(valor)

        if tipo == 'dd':
            if valor > 0 and valor <= 31:
                self.dia = valor
            else:
                print("Día inválido.")
        elif tipo == 'mm':
            if valor > 0 and valor <= 12:
                self.mes = valor
            else:
                print("Mes inválido.")
        elif tipo == 'aaaa':
            if valor >= 0:
                self.anio = valor
            else:
                print("Año inválido.")
        elif tipo == 'HH':
            if valor >= 0 and valor < 24:
                self.hora = valor
            else:
                print("Hora inválida.")
        elif tipo == 'MM':
            if valor >= 0 and valor < 60:
                self.minuto = valor
            else:
                print("Minuto inválido.")
        elif tipo == 'SS':
            if valor >= 0 and valor < 60:
                self.segundo = valor
            else:
                print("Segundo inválido.")
        else:
            print("Parámetro inválido.")

    def __str__(self):
        fecha = "{:04d}/{:02d}/{:02d}".format(self.anio, self.mes, self.dia)
        hora = "{:02d}:{:02d}:{:02d}".format(self.hora, self.minuto, self.segundo)
        return fecha + ' ' + hora


if __name__ == "__main__":
    fecha_hora = FechaHora(1, 1, 2022, 12, 30, 0)
    print(fecha_hora)

    fecha_hora.fijarFecha('15/06/2023')
    fecha_hora.fijarHora('18:45:30')
    print(fecha_hora)

    fecha_hora.fijarFechaHora('31/12/2024 23:59:59')
    print(fecha_hora)

    fecha_hora.cambiar('dd=40')
    fecha_hora.cambiar('mm=13')
    fecha_hora.cambiar('aaaa=-2022')
    fecha_hora.cambiar('HH=25')
    fecha_hora.cambiar('MM=70')
    fecha_hora.cambiar('SS=90')

    print(fecha_hora)