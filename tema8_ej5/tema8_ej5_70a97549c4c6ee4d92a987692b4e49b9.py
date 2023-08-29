class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        if '/' in fecha_str:
            dia, mes, anio = fecha_str.split('/')
        elif '-' in fecha_str:
            dia, mes, anio = fecha_str.split('-')
        else:
            raise ValueError("Formato de fecha inválido. Utilice dd/mm/aaaa o dd-mm-aaaa.")

        self.fecha = {
            'dia': int(dia),
            'mes': int(mes),
            'anio': int(anio)
        }

    def fijarHora(self, hora_str):
        if ':' not in hora_str:
            raise ValueError("Formato de hora inválido. Utilice HH:MM:SS.")

        hora, minutos, segundos = hora_str.split(':')
        self.hora = {
            'hora': int(hora),
            'minutos': int(minutos),
            'segundos': int(segundos)
        }

    def fijarFechaHora(self, fecha_hora_str):
     
        fecha_str, hora_str = fecha_hora_str.split()

        self.fijarFecha(fecha_str)
        self.fijarHora(hora_str)

    def cambiar(self, cambio_str):
        parametro, valor = cambio_str.split('=')
        parametro = parametro.strip().lower()
        valor = int(valor)

        if self.fecha is None or self.hora is None:
            raise ValueError("La fecha y la hora deben ser establecidas primero.")

        if parametro == 'dd':
            if valor < 1 or valor > 31:
                raise ValueError("El valor del día debe estar entre 1 y 31.")
            self.fecha['dia'] = valor
        elif parametro == 'mm':
            if valor < 1 or valor > 12:
               print("El valor del mes debe estar entre 1 y 12.")
            self.fecha['mes'] = valor
        elif parametro == 'aaaa':
            if valor < 1:
                raise ValueError("El valor del año debe ser positivo.")
            self.fecha['anio'] = valor
        elif parametro == 'hh':
            if valor < 0 or valor > 23:
                raise ValueError("El valor de la hora debe estar entre 0 y 23.")
            self.hora['hora'] = valor
        elif parametro == 'mm':
            if valor < 0 or valor > 59:
                raise ValueError("El valor de los minutos debe estar entre 0 y 59.")
            self.hora['minutos'] = valor
        elif parametro == 'ss':
            if valor < 0 or valor > 59:
                raise ValueError("El valor de los segundos debe estar entre 0 y 59.")
            self.hora['segundos'] = valor
        else:
            raise ValueError("Parámetro inválido. Utilice dd, mm, aaaa, hh, mm o ss.")

    def __str__(self):
        if self.fecha is None or self.hora is None:
            return "Fecha y hora no establecidas."

        fecha_str = "{:04d}/{:02d}/{:02d}".format(self.fecha['anio'], self.fecha['mes'], self.fecha['dia'])
        hora_str = "{:02d}:{:02d}:{:02d}".format(self.hora['hora'], self.hora['minutos'], self.hora['segundos'])
        return fecha_str + ' ' + hora_str

fecha_hora = FechaHora()
fecha_hora.fijarFecha('10/06/2023')
fecha_hora.fijarHora('12:30:00')
print(fecha_hora)  

fecha_hora.fijarFechaHora('15-12-2023 23:45:10')
print(fecha_hora)  

fecha_hora.cambiar('dd=25')
print(fecha_hora)  

fecha_hora.cambiar('mm=13')