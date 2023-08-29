class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        # Validar el formato de fecha
        if '/' in fecha_str:
            dia, mes, anio = fecha_str.split('/')
        elif '-' in fecha_str:
            dia, mes, anio = fecha_str.split('-')
        else:
            raise ValueError("El formato de fecha no es válido. Utilice 'dd/mm/aaaa' o 'dd-mm-aaaa'.")
        
        # Convertir a enteros
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
        
        # Validar los valores de día, mes y año
        if not (1 <= dia <= 31):
            raise ValueError("El día debe estar en el rango de 1 a 31.")
        if not (1 <= mes <= 12):
            raise ValueError("El mes debe estar en el rango de 1 a 12.")
        if not (1 <= anio):
            raise ValueError("El año debe ser mayor que 0.")
        
        self.fecha = (anio, mes, dia)

    def fijarHora(self, hora_str):
        # Validar el formato de hora
        if ':' not in hora_str:
            raise ValueError("El formato de hora no es válido. Utilice 'HH:MM:SS'.")
        
        # Dividir las partes de la hora
        partes_hora = hora_str.split(':')
        
        # Convertir a enteros
        horas = int(partes_hora[0])
        minutos = int(partes_hora[1])
        segundos = int(partes_hora[2])
        
        # Validar los valores de hora, minutos y segundos
        if not (0 <= horas < 24):
            raise ValueError("Las horas deben estar en el rango de 0 a 23.")
        if not (0 <= minutos < 60):
            raise ValueError("Los minutos deben estar en el rango de 0 a 59.")
        if not (0 <= segundos < 60):
            raise ValueError("Los segundos deben estar en el rango de 0 a 59.")
        
        self.hora = (horas, minutos, segundos)

    def fijarFechaHora(self, fecha_hora_str):
        # Dividir la cadena en fecha y hora
        fecha_str, hora_str = fecha_hora_str.split()
        
        # Llamar a los métodos fijarFecha y fijarHora
        self.fijarFecha(fecha_str)
        self.fijarHora(hora_str)

    def cambiar(self, parametro):
        # Dividir el parámetro en el nombre del parámetro y su valor
        nombre_parametro, valor = parametro.split('=')
        
        # Eliminar espacios alrededor del nombre del parámetro y valor
        nombre_parametro = nombre_parametro.strip()
        valor = valor.strip()
        
        # Comprobar qué parámetro se quiere cambiar y validar su valor
        if nombre_parametro == 'dd':
            dia = int(valor)
            if not (1 <= dia <= 31):
                raise ValueError("El día debe estar en el rango de 1 a 31.")
            _, mes, anio = self.fecha
            self.fecha = (anio, mes, dia)
        elif nombre_parametro == 'mm':
            mes = int
