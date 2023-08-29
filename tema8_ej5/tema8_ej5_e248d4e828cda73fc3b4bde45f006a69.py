class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha):
        # Validar formato de fecha
        if '/' in fecha:
            dia, mes, anio = fecha.split('/')
        elif '-' in fecha:
            dia, mes, anio = fecha.split('-')
        else:
            print("Formato de fecha incorrecto. Debe ser dd/mm/aaaa o dd-mm-aaaa.")
            return

        # Validar día, mes y año
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 0:
            print("Fecha inválida.")
            return

        self.fecha = (dia, mes, anio)

    def fijarHora(self, hora):
        # Validar formato de hora
        if ':' not in hora:
            print("Formato de hora incorrecto. Debe ser HH:MM:SS.")
            return

        # Validar hora, minuto y segundo
        hh, mm, ss = hora.split(':')
        hh = int(hh)
        mm = int(mm)
        ss = int(ss)
        if hh < 0 or hh > 23 or mm < 0 or mm > 59 or ss < 0 or ss > 59:
            print("Hora inválida.")
            return

        self.hora = (hh, mm, ss)

    def fijarFechaHora(self, fecha_hora):
        # Validar formato de fecha y hora
        if ' ' not in fecha_hora or ':' not in fecha_hora:
            print("Formato de fecha y hora incorrecto. Debe ser dd/mm/aaaa HH:MM:SS.")
            return

        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        # Validar formato de parámetro
        if '=' not in parametro:
            print("Formato de parámetro incorrecto. Debe ser <tipo>=<valor>.")
            return

        tipo, valor = parametro.split('=')
        tipo = tipo.strip()
        valor = valor.strip()

        if tipo == 'dd':
            dia, mes, anio = self.fecha
            dia = int(valor)
            if dia < 1 or dia > 31:
                print("Día inválido.")
                return
            self.fecha = (dia, mes, anio)
        elif tipo == 'mm':
            dia, mes, anio = self.fecha
            mes = int(valor)
            if mes < 1 or mes > 12:
                print("Mes inválido.")
                return
            self.fecha = (dia, mes, anio)
        elif tipo == 'aaaa':
            dia, mes, anio = self.fecha
            anio = int(valor)
            if anio < 0:
                print("Año inválido.")
                return
            self.fecha = (dia, mes, anio)
        elif tipo == 'HH':
            hh, mm, ss = self.hora
            hh = int(valor)
            if hh < 0 or hh > 23:
                print("Hora inválida.")
                return
            self.hora = (hh, mm, ss)
        elif tipo == 'MM':
           

           