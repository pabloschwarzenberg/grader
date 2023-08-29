class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        # Validar el formato de fecha dd/mm/aaaa o dd-mm-aaaa
        if '/' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('/'))
        elif '-' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('-'))
        else:
            raise ValueError("Formato de fecha inválido")

    def fijarHora(self, hora):
        # Validar el formato de hora HH:MM:SS
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        # Validar el formato de fecha y hora dd/mm/aaaa HH:MM:SS
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        # Obtener el tipo de parámetro y su valor
        parametro = parametro.replace(' ', '')  # Eliminar espacios en blanco
        tipo, valor = parametro.split('=')

        # Validar y cambiar el parámetro correspondiente
        if tipo == 'dd':
            nuevo_dia = int(valor)
            if 1 <= nuevo_dia <= 31:
                self.dia = nuevo_dia
            else:
                print("Día inválido")
        elif tipo == 'mm':
            nuevo_mes = int(valor)
            if 1 <= nuevo_mes <= 12:
                self.mes = nuevo_mes
            else:
                print("Mes inválido")
        elif tipo == 'aaaa':
            nuevo_anio = int(valor)
            if 1900 <= nuevo_anio <= 9999:
                self.anio = nuevo_anio
            else:
                print("Año inválido")
        elif tipo == 'HH':
            nueva_hora = int(valor)
            if 0 <= nueva_hora <= 23:
                self.hora = nueva_hora
            else:
                print("Hora inválida")
        elif tipo == 'MM':
            nuevo_minuto = int(valor)
            if 0 <= nuevo_minuto <= 59:
                self.minuto = nuevo_minuto
            else:
                print("Minuto inválido")
        elif tipo == 'SS':
            nuevo_segundo = int(valor)
            if 0 <= nuevo_segundo <= 59:
                self.segundo = nuevo_segundo
            else:
                print("Segundo inválido")
        else:
            print("Tipo de parámetro inválido")

    def __str__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
