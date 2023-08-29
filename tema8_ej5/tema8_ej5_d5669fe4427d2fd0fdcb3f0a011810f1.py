class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        # Validar formato dd/mm/aaaa o dd-mm-aaaa
        if '/' in fecha_str:
            dia, mes, anio = fecha_str.split('/')
        elif '-' in fecha_str:
            dia, mes, anio = fecha_str.split('-')
        else:
            raise ValueError("Formato de fecha inválido. Debe ser dd/mm/aaaa o dd-mm-aaaa.")

        # Convertir a enteros
        dia, mes, anio = int(dia), int(mes), int(anio)

        # Validar día, mes y año
        if not (1 <= dia <= 31):
            raise ValueError("Día inválido.")
        if not (1 <= mes <= 12):
            raise ValueError("Mes inválido.")
        if not (1900 <= anio <= 2100):
            raise ValueError("Año inválido.")

        self.fecha = (anio, mes, dia)

    def fijarHora(self, hora_str):
        # Validar formato HH:MM:SS
        hora, minuto, segundo = map(int, hora_str.split(':'))

        # Validar hora, minuto y segundo
        if not (0 <= hora <= 23):
            raise ValueError("Hora inválida.")
        if not (0 <= minuto <= 59):
            raise ValueError("Minuto inválido.")
        if not (0 <= segundo <= 59):
            raise ValueError("Segundo inválido.")

        self.hora = (hora, minuto, segundo)

    def fijarFechaHora(self, fecha_hora_str):
        # Validar formato dd/mm/aaaa HH:MM:SS
        fecha_str, hora_str = fecha_hora_str.split(' ')
        self.fijarFecha(fecha_str)
        self.fijarHora(hora_str)

    def cambiar(self, parametro):
        # Obtener tipo de parámetro y valor
        tipo, valor = parametro.split('=')
        tipo = tipo.strip().lower()
        valor = valor.strip()

        # Validar y cambiar el parámetro correspondiente
        if tipo == 'dd':
            dia = int(valor)
            if not (1 <= dia <= 31):
                raise ValueError("Día inválido.")
            anio, mes, _ = self.fecha
            self.fecha = (anio, mes, dia)
        elif tipo == 'mm':
            mes = int(valor)
            if not (1 <= mes <= 12):
                raise ValueError("Mes inválido.")
            anio, _, dia = self.fecha
            self.fecha = (anio, mes, dia)
        elif tipo == 'aaaa':
            anio = int(valor)
            if not (1900 <= anio <= 2100):
                raise ValueError("Año inválido.")
            _, mes, dia = self.fecha
            self.fecha = (anio, mes, dia)
        elif tipo == 'hh':
            hora = int(valor)
            if not (0 <= hora <= 23):
                raise ValueError("Hora inválida.")
            minuto, segundo = self.hora[1:]
            self.hora = (hora, minuto, segundo)
        elif tipo == 'mm':
            minuto = int(valor)
            if not (0 <= minuto <= 59):
                raise ValueError("Minuto inválido.")
            hora, segundo = self.hora[::2]
            self.hora = (hora
