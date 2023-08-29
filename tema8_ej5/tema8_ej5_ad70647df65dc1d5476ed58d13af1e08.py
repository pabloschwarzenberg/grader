class FechaHora:
    def __init__(self, fecha='', hora=''):
        self.dia = 1
        self.mes = 1
        self.anio = 2000
        self.hora = 0
        self.minutos = 0
        self.segundos = 0

        if fecha:
            self.fijarFecha(fecha)

        if hora:
            self.fijarHora(hora)

    def fijarFecha(self, fecha):
        separador = '/' if '/' in fecha else '-'
        partes = fecha.split(separador)

        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(':')

        self.hora = int(partes[0])
        self.minutos = int(partes[1])
        self.segundos = int(partes[2])

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(' ')

        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parametro):
        partes = parametro.split('=')

        if len(partes) != 2:
            print("Error: Formato de parámetro inválido.")
            return

        nombre = partes[0].strip().lower()
        valor = partes[1].strip()

        if nombre == 'dd':
            dia = int(valor)
            if dia >= 1 and dia <= 31:
                self.dia = dia
            else:
                print("Error: El día debe estar entre 1 y 31.")
        elif nombre == 'mm':
            mes = int(valor)
            if mes >= 1 and mes <= 12:
                self.mes = mes
            else:
                print("Error: El mes debe estar entre 1 y 12.")
        elif nombre == 'aaaa':
            anio = int(valor)
            self.anio = anio
        elif nombre == 'hh':
            hora = int(valor)
            if hora >= 0 and hora <= 23:
                self.hora = hora
            else:
                print("Error: La hora debe estar entre 0 y 23.")
        elif nombre == 'mm':
            minutos = int(valor)
            if minutos >= 0 and minutos <= 59:
                self.minutos = minutos
            else:
                print("Error: Los minutos deben estar entre 0 y 59.")
        elif nombre == 'ss':
            segundos = int(valor)
            if segundos >= 0 and segundos <= 59:
                self.segundos = segundos
            else:
                print("Error: Los segundos deben estar entre 0 y 59.")
        else:
            print("Error: Nombre de parámetro inválido.")

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(self.anio, self.mes, self.dia, self.hora,
                                                                  self.minutos, self.segundos)


fecha_hora = FechaHora()
fecha_hora.fijarFecha('01/05/2023')
fecha_hora.fijarHora('10:30:00')
print(fecha_hora)


