class FechaHora:
    def __init__(self, fecha=None, hora=None):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minutos = None
        self.segundos = None

        if fecha:
            self.fijarFecha(fecha)
        if hora:
            self.fijarHora(hora)

    def fijarFecha(self, fecha):
        if '/' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('/'))
        elif '-' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('-'))
        else:
            raise ValueError("Formato de fecha inválido. Debe ser dd/mm/aaaa o dd-mm-aaaa")

    def fijarHora(self, hora):
        self.hora, self.minutos, self.segundos = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        parametro = parametro.replace(' ', '')
        tipo, valor = parametro.split('=')

        if tipo == 'dd':
            nuevo_dia = int(valor)
            if 1 <= nuevo_dia <= 31:
                self.dia = nuevo_dia
            else:
                print("Día inválido. Debe ser un valor entre 1 y 31.")
        elif tipo == 'mm':
            nuevo_mes = int(valor)
            if 1 <= nuevo_mes <= 12:
                self.mes = nuevo_mes
            else:
                print("Mes inválido. Debe ser un valor entre 1 y 12.")
        elif tipo == 'aaaa':
            nuevo_anio = int(valor)
            self.anio = nuevo_anio
        elif tipo == 'HH':
            nueva_hora = int(valor)
            if 0 <= nueva_hora <= 23:
                self.hora = nueva_hora
            else:
                print("Hora inválida. Debe ser un valor entre 0 y 23.")
        elif tipo == 'MM':
            nuevos_minutos = int(valor)
            if 0 <= nuevos_minutos <= 59:
                self.minutos = nuevos_minutos
            else:
                print("Minutos inválidos. Debe ser un valor entre 0 y 59.")
        elif tipo == 'SS':
            nuevos_segundos = int(valor)
            if 0 <= nuevos_segundos <= 59:
                self.segundos = nuevos_segundos
            else:
                print("Segundos inválidos. Debe ser un valor entre 0 y 59.")
        else:
            print("Parámetro inválido.")

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minutos, self.segundos
        )
