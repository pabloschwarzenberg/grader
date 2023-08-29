class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1970
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        partes = fecha.split('/')
        if len(partes) != 3:
            partes = fecha.split('-')
        if len(partes) != 3:
            raise ValueError("El formato de fecha debe ser dd/mm/aaaa o dd-mm-aaaa")

        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(':')
        if len(partes) != 3:
            raise ValueError("El formato de hora debe ser HH:MM:SS")

        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(' ')
        if len(partes) != 2:
            raise ValueError("El formato de fecha y hora debe ser dd/mm/aaaa HH:MM:SS")

        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parametro):
        partes = parametro.split('=')
        if len(partes) != 2:
            raise ValueError("El formato de cambio debe ser tipo=valor")

        tipo = partes[0].strip()
        valor = partes[1].strip()

        if tipo == 'dd':
            dia = int(valor)
            if 1 <= dia <= 31:
                self.dia = dia
            else:
                raise ValueError("El día debe estar entre 1 y 31")
        elif tipo == 'mm':
            mes = int(valor)
            if 1 <= mes <= 12:
                self.mes = mes
            else:
                raise ValueError("El mes debe estar entre 1 y 12")
        elif tipo == 'aaaa':
            anio = int(valor)
            if anio >= 1970:
                self.anio = anio
            else:
                raise ValueError("El año debe ser igual o mayor a 1970")
        elif tipo == 'HH':
            hora = int(valor)
            if 0 <= hora <= 23:
                self.hora = hora
            else:
                raise ValueError("La hora debe estar entre 0 y 23")
        elif tipo == 'MM':
            minuto = int(valor)
            if 0 <= minuto <= 59:
                self.minuto = minuto
            else:
                raise ValueError("Los minutos deben estar entre 0 y 59")
        elif tipo == 'SS':
            segundo = int(valor)
            if 0 <= segundo <= 59:
                self.segundo = segundo
            else:
                raise ValueError("Los segundos deben estar entre 0 y 59")
        else:
            raise ValueError("Tipo de parámetro inválido")


    def __str__(self):
        elmes = str(self.mes)
        if len(elmes) < 2:
            elmes = "0"+elmes
        eldia = str(self.dia)
        if len(eldia) < 2:
            eldia = "0"+eldia
        elsegundo = str(self.segundo)
        if len(elsegundo) < 2:
            elsegundo = "0"+elsegundo
        elminuto = str(self.minuto)
        if len(elminuto) < 2:
            elminuto = "0"+elminuto            

        fecha = str(self.anio)+"/"+str(elmes)+"/"+str(eldia)
        hora = str(self.hora)+":"+elminuto+":"+elsegundo
        return fecha+" "+hora
