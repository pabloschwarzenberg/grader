class FechaHora:
    def __init__(self, fecha, hora):
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def fijarFecha(self, fecha):
        try:
            separador = '/' if '/' in fecha else '-'
            dia, mes, anio = fecha.split(separador)
            self.dia = int(dia)
            self.mes = int(mes)
            self.anio = int(anio)
        except ValueError:
            raise ValueError("El formato de fecha ingresado no es válido.")

    def fijarHora(self, hora):
        try:
            horas, minutos, segundos = hora.split(':')
            self.horas = int(horas)
            self.minutos = int(minutos)
            self.segundos = int(segundos)
        except ValueError:
            raise ValueError("El formato de hora ingresado no es válido.")

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        try:
            clave, valor = parametro.split('=')
            valor = int(valor.strip())
            
            if clave == 'dd':
                if valor < 1 or valor > 31:
                    raise ValueError("El día debe estar entre 1 y 31.")
                self.dia = valor
            elif clave == 'mm':
                if valor < 1 or valor > 12:
                    raise ValueError("El mes debe estar entre 1 y 12.")
                self.mes = valor
            elif clave == 'aaaa':
                self.anio = valor
            elif clave == 'HH':
                if valor < 0 or valor > 23:
                    raise ValueError("La hora debe estar entre 0 y 23.")
                self.horas = valor
            elif clave == 'MM':
                if valor < 0 or valor > 59:
                    raise ValueError("Los minutos deben estar entre 0 y 59.")
                self.minutos = valor
            elif clave == 'SS':
                if valor < 0 or valor > 59:
                    raise ValueError("Los segundos deben estar entre 0 y 59.")
                self.segundos = valor
            else:
                raise ValueError("El parámetro ingresado no es válido.")
        except ValueError:
            raise ValueError("El formato del parámetro es inválido.")

    def __str__(self):
        fecha = f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d}"
        hora = f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"
        return f"{fecha} {hora}"
# Crear un objeto FechaHora
fecha_hora = FechaHora("25/05/2023", "12:30:45")

print(fecha_hora)  # Mostrar la fecha y hora actual

# Cambiar el día a 2
fecha_hora.cambiar("dd=2")

# Cambiar el mes a 10
fecha_hora.cambiar("mm=10")

# Cambiar el año a 2024
fecha_hora.cambiar("aaaa=2024")

# Cambiar la hora a 18
fecha_hora.cambiar("HH=18")

# Cambiar los minutos a 15
fecha_hora.cambiar
