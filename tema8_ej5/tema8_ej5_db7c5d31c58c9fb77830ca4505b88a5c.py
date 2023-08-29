class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None
    
    def fijarFecha(self, fecha_str):
        self.fecha = self.validarFecha(fecha_str)
    
    def fijarHora(self, hora_str):
        self.hora = self.validarHora(hora_str)
    
    def fijarFechaHora(self, fecha_hora_str):
        fecha_hora = fecha_hora_str.split(' ')
        self.fijarFecha(fecha_hora[0])
        self.fijarHora(fecha_hora[1])
    
    def cambiar(self, parametro):
        if parametro.startswith('dd='):
            dia = int(parametro.split('=')[1])
            if self.validarDia(dia):
                self.fecha[0] = dia
            else:
                print('Error: El día especificado es inválido.')
        elif parametro.startswith('mm='):
            mes = int(parametro.split('=')[1])
            if self.validarMes(mes):
                self.fecha[1] = mes
            else:
                print('Error: El mes especificado es inválido.')
        elif parametro.startswith('aaaa='):
            anio = int(parametro.split('=')[1])
            if self.validarAnio(anio):
                self.fecha[2] = anio
            else:
                print('Error: El año especificado es inválido.')
        elif parametro.startswith('HH='):
            hora = int(parametro.split('=')[1])
            if self.validarHora(hora):
                self.hora[0] = hora
            else:
                print('Error: La hora especificada es inválida.')
        elif parametro.startswith('MM='):
            minutos = int(parametro.split('=')[1])
            if self.validarMinutos(minutos):
                self.hora[1] = minutos
            else:
                print('Error: Los minutos especificados son inválidos.')
        elif parametro.startswith('SS='):
            segundos = int(parametro.split('=')[1])
            if self.validarSegundos(segundos):
                self.hora[2] = segundos
            else:
                print('Error: Los segundos especificados son inválidos.')
        else:
            print('Error: El parámetro especificado no es válido.')
    
    def __str__(self):
        fecha_str = '/'.join(str(x).zfill(2) for x in self.fecha)
        hora_str = ':'.join(str(x).zfill(2) for x in self.hora)
        return f'{fecha_str} {hora_str}'
    
    @staticmethod
    def validarFecha(fecha_str):
        try:
            dia, mes, anio = map(int, fecha_str.split('/') if '/' in fecha_str else fecha_str.split('-'))
            if FechaHora.validarDia(dia) and FechaHora.validarMes(mes) and FechaHora.validarAnio(anio):
                return [dia, mes, anio]
            else:
                raise ValueError('Fecha inválida.')
        except ValueError:
            raise ValueError('Formato de fecha inválido.')
    
    @staticmethod
    def validarDia(dia):
        return 1 <= dia <= 31
    
    @staticmethod
    def validarMes(mes):
        return 1 <= mes <= 12
    
    @staticmethod
    def validarAnio(anio):
        return anio >= 0
    
    @staticmethod
    def validarHora(hora_str):
        try:
            hora, minutos, segundos = map(int, hora_str.split(':'))
           
