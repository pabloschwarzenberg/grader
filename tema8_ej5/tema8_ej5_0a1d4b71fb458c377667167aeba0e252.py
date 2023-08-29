class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        fecha_str = fecha_str.replace('-', '/')
        self.fecha = fecha_str

    def fijarHora(self, hora_str):
        self.hora = hora_str

    def fijarFechaHora(self, fechahora_str):
        fecha_str, hora_str = fechahora_str.split()
        self.fijarFecha(fecha_str)
        self.fijarHora(hora_str)

    def cambiar(self, parametro):
        parametro = parametro.replace(' ', '')
        tipo, valor = parametro.split('=')
        if tipo == 'dd':
            dia, mes, anio = self.fecha.split('/')
            dia = valor.zfill(2)
            self.fecha = dia + '/' + mes + '/' + anio
        elif tipo == 'mm':
            dia, mes, anio = self.fecha.split('/')
            mes = valor.zfill(2)
            self.fecha = dia + '/' + mes + '/' + anio
        elif tipo == 'aaaa':
            dia, mes, anio = self.fecha.split('/')
            anio = valor
            self.fecha = dia + '/' + mes + '/' + anio
        elif tipo == 'HH':
            hora, minuto, segundo = self.hora.split(':')
            hora = valor.zfill(2)
            self.hora = hora + ':' + minuto + ':' + segundo
        elif tipo == 'MM':
            hora, minuto, segundo = self.hora.split(':')
            minuto = valor.zfill(2)
            self.hora = hora + ':' + minuto + ':' + segundo
        elif tipo == 'SS':
            hora, minuto, segundo = self.hora.split(':')
            segundo = valor.zfill(2)
            self.hora = hora + ':' + minuto + ':' + segundo
        else:
            print('Parámetro ' + tipo + ' no válido')

    def __str__(self):
        dia, mes, anio = self.fecha.split('/')
        return anio + '/' + mes + '/' + dia + ' ' + self.hora
