from copy import deepcopy
class FechaHora:
    def __init__(self):
        self.fecha = ['dd', 'mm', 'aaaa']
        self.hora = ['HH', 'MM', 'SS']

    def __str__(self):
        fecha  = deepcopy(self.fecha)
        fecha.reverse()
        fecha = '/'.join(fecha)
        hora = ':'.join(self.hora)
        return fecha + ' ' + hora

    def fijarFecha(self, fecha):
        if '/' in fecha:
            self.fecha = fecha.split('/')
        else:
            self.fecha = fecha.split('-')

    def fijarHora(self, hora):
        self.hora = hora.split(':')

    def fijarFechaHora(self, fechahora):
        fechahora = fechahora.split(' ')
        self.fijarFecha(fechahora[0])
        self.fijarHora(fechahora[1])

    def cambiar(self, parte):
        parte = parte.split('=')
        if parte[0].strip() == 'dd':
            self.fecha[0] = parte[1].strip()
        elif parte[0].strip() == 'mm':
            self.fecha[1] = parte[1].strip()
        elif parte[0].strip() == 'aaaa':
            self.fecha[2] = parte[1].strip()
        elif parte[0].strip() == 'HH':
            self.hora[0] = parte[1].strip()
        elif parte[0].strip() == 'MM':
            self.hora[1] = parte[1].strip()
        elif parte[0].strip() == 'SS':
            self.hora[2] = parte[1].strip()