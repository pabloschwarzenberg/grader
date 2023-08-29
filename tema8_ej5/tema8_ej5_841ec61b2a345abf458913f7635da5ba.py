import datetime

class FechaHora:
    def __init__(self, fecha, hora):
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def fijarFecha(self, fecha):
        self.dia, self.mes, self.anio = map(int, fecha.split('/'))

    def fijarHora(fecha_hora ):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        parametros = {
            'dd': lambda x: setattr(self, 'dia', int(x)) if int(x) <= 31 else print("Error: El día ingresado es inválido."),
            'mm': lambda x: setattr(self, 'mes', int(x)) if int(x) <= 12 else print("Error: El mes ingresado es inválido."),
            'aaaa': lambda x: setattr(self, 'anio', int(x)),
            'hh': lambda x: setattr(self, 'hora', int(x)) if int(x) <= 23 else print("Error: La hora ingresada es inválida."),
            'MM': lambda x: setattr(self, 'minuto', int(x)) if int(x) <= 59 else print("Error: El minuto ingresado es inválido."),
            'ss': lambda x: setattr(self, 'segundo', int(x)) if int(x) <= 59 else print("Error: El segundo ingresado es inválido."),
        }
        tipo, valor = parametro.replace(' ', '').split('=')
        tipo = tipo.lower()
        parametros.get(tipo, lambda x: print("Error: El parámetro ingresado no es válido."))(valor)

    def __repr__(self):
        fecha = "{:04d}/{:02d}/{:02d}".format(self.anio, self.mes, self.dia)
        hora = "{:02d}:{:02d}:{:02d}".format(self.hora, self.minuto, self.segundo)
        return "{} {}".format(fecha, hora)