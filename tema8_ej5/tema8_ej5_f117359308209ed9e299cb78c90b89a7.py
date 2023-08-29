class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        if self.fecha is None or self.hora is None:
            return "Fecha y hora no establecidas."
        fecha_str = f"{self.fecha[0]:04d}/{self.fecha[1]:02d}/{self.fecha[2]:02d}"
        hora_str = f"{self.hora[0]:02d}:{self.hora[1]:02d}:{self.hora[2]:02d}"
        return f"{fecha_str} {hora_str}"

    def fijarFecha(self, fecha):
        try:
            dia, mes, anio = fecha.split('/')
        except ValueError:
            try:
                dia, mes, anio = fecha.split('-')
            except ValueError:
                print("Formato de fecha inválido. Debe ser dd/mm/aaaa o dd-mm-aaaa.")
                return

        try:
            dia = int(dia)
            mes = int(mes)
            anio = int(anio)
        except ValueError:
            print("Formato de fecha inválido. Los valores de día, mes y año deben ser numéricos.")
            return

        if dia < 1 or dia > 31:
            print("Día inválido.")
            return
        if mes < 1 or mes > 12:
            print("Mes inválido.")
            return
        if anio < 0:
            print("Año inválido.")
            return

        self.fecha = (anio, mes, dia)

    def fijarHora(self, hora):
        try:
            horas, minutos, segundos = hora.split(':')
        except ValueError:
            print("Formato de hora inválido. Debe ser HH:MM:SS.")
            return

        try:
            horas = int(horas)
            minutos = int(minutos)
            segundos = int(segundos)
        except ValueError:
            print("Formato de hora inválido. Los valores de hora, minuto y segundo deben ser numéricos.")
            return

        if horas < 0 or horas > 23:
            print("Hora inválida.")
            return
        if minutos < 0 or minutos > 59:
            print("Minuto inválido.")
            return
        if segundos < 0 or segundos > 59:
            print("Segundo inválido.")
            return

        self.hora = (horas, minutos, segundos)

    def fijarFechaHora(self, fechahora):
        try:
            fecha_str, hora_str = fechahora.split(' ')
        except ValueError:
            print("Formato de fecha y hora inválido. Debe ser dd/mm/aaaa HH:MM:SS.")
            return

        self.fijarFecha(fecha_str)
        self.fijarHora(hora_str)

    def cambiar(self, parte):
        partes_permitidas = ["dd", "mm", "aaaa", "HH", "MM", "SS"]
        try:
            parametro, valor = parte.replace(" ", "").split('=')
            parametro = parametro.lower()
            valor = int(valor)
        except ValueError:
            print("Formato de cambio inválido. Debe ser 'tipo=valor'.")
            return

        if parametro not in partes_permitidas:
            print("Parámetro no válido. Los parámetros permitidos son: dd, mm, aaaa, HH, MM, SS.")
            return

        if parametro == "dd" and (valor < 1 or
