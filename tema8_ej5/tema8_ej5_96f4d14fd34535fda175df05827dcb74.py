class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        # Validar formato de fecha
        try:
            dia, mes, anio = fecha_str.split('/')  # Separar por '/'
        except ValueError:
            try:
                dia, mes, anio = fecha_str.split('-')  # Separar por '-'
            except ValueError:
                raise ValueError("Formato de fecha inválido. Debe ser dd/mm/aaaa o dd-mm-aaaa")

        # Validar valores de día, mes y año
        if not (1 <= int(dia) <= 31) or not (1 <= int(mes) <= 12) or not (1 <= int(anio) <= 9999):
            raise ValueError("Fecha inválida")

        self.fecha = f"{anio}/{mes}/{dia}"

    def fijarHora(self, hora_str):
        # Validar formato de hora
        try:
            horas, minutos, segundos = hora_str.split(':')
        except ValueError:
            raise ValueError("Formato de hora inválido. Debe ser HH:MM:SS")

        # Validar valores de hora, minutos y segundos
        if not (0 <= int(horas) < 24) or not (0 <= int(minutos) < 60) or not (0 <= int(segundos) < 60):
            raise ValueError("Hora inválida")

        self.hora = hora_str

    def fijarFechaHora(self, fecha_hora_str):
        try:
            fecha_str, hora_str = fecha_hora_str.split(' ')
            self.fijarFecha(fecha_str)
            self.fijarHora(hora_str)
        except ValueError:
            raise ValueError("Formato de fecha y hora inválido. Debe ser dd/mm/aaaa HH:MM:SS")

    def cambiar(self, parametro):
        # Obtener tipo de parámetro y su valor
        tipo, valor = parametro.strip().split('=')

        # Validar y cambiar el parámetro correspondiente
        if tipo.lower() == 'dd':
            dia = int(valor)
            if not (1 <= dia <= 31):
                raise ValueError("Día inválido")
            self.fecha = self.fecha[:8] + str(dia).zfill(2)
        elif tipo.lower() == 'mm':
            mes = int(valor)
            if not (1 <= mes <= 12):
                raise ValueError("Mes inválido")
            self.fecha = self.fecha[:5] + str(mes).zfill(2) + self.fecha[7:]
        elif tipo.lower() == 'aaaa':
            anio = int(valor)
            if not (1 <= anio <= 9999):
                raise ValueError("Año inválido")
            self.fecha = str(anio) + self.fecha[4:]
        elif tipo.lower() == 'hh':
            horas = int(valor)
            if not (0 <= horas < 24):
                raise ValueError("Hora inválida")
            self.hora = str(horas).zfill(2) + self.hora[2:]
        elif tipo.lower() == 'MM':
            minutos = int(valor)
            if not (0 <= minutos < 60):
                raise ValueError("Minutos inválidos")
            self.hora = self.hora[:3] + str(minutos).zfill(2) + self.hora[5:]
        elif tipo.lower() == 'ss':
            segundos = int(valor)
            if not (0 <= segundos < 60):
                raise ValueError("Segundos inválidos")
            self.hora = self.hora[:6] + str(segundos).zfill(2)
        else:
            raise ValueError("Parámetro desconocido")

    def __str__(self):
        return f"{self.fecha} {self.hora}"


# Ejemplo de uso:
fecha_hora = FechaHora()
fecha_hora.fijarFecha('20/06/2023')
fecha_hora.fijarHora('12:30:45')
fecha_hora.cambiar('dd=25')
fecha_hora.cambiar('hh=8')
print(fecha_hora)  # Salida: 2023/06/25 08:30:45

