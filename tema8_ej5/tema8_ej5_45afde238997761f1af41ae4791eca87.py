class FechaHora:
    def __init__(self):
        self.fecha = ''
        self.hora = ''

    def fijarFecha(self, fecha):
        # Validar el formato de la fecha
        if self.validarFormatoFecha(fecha):
            self.fecha = fecha
        else:
            print("Formato de fecha incorrecto. Utilice el formato dd/mm/aaaa o dd-mm-aaaa.")

    def fijarHora(self, hora):
        # Validar el formato de la hora
        if self.validarFormatoHora(hora):
            self.hora = hora
        else:
            print("Formato de hora incorrecto. Utilice el formato HH:MM:SS.")

    def fijarFechaHora(self, fecha_hora):
        # Dividir la cadena en fecha y hora
        partes = fecha_hora.split(' ')
        if len(partes) != 2:
            print("Formato de fecha y hora incorrecto. Utilice el formato dd/mm/aaaa HH:MM:SS.")
            return

        fecha = partes[0]
        hora = partes[1]

        # Validar el formato de la fecha y la hora
        if self.validarFormatoFecha(fecha) and self.validarFormatoHora(hora):
            self.fecha = fecha
            self.hora = hora
        else:
            print("Formato de fecha y hora incorrecto. Utilice el formato dd/mm/aaaa HH:MM:SS.")

    def cambiar(self, parametro):
        # Dividir el parámetro en tipo y valor
        partes = parametro.split('=')
        if len(partes) != 2:
            print("Formato de cambio incorrecto. Utilice el formato tipo=valor.")
            return

        tipo = partes[0].strip()
        valor = partes[1].strip()

        if tipo == 'dd':
            # Validar y cambiar el día
            if self.validarDia(valor):
                self.fecha = self.fecha[:2] + valor + self.fecha[4:]
            else:
                print("Día inválido.")
        elif tipo == 'mm':
            # Validar y cambiar el mes
            if self.validarMes(valor):
                self.fecha = valor + self.fecha[2:5] + self.fecha[5:]
            else:
                print("Mes inválido.")
        elif tipo == 'aaaa':
            # Validar y cambiar el año
            if self.validarAnio(valor):
                self.fecha = self.fecha[:6] + valor
            else:
                print("Año inválido.")
        elif tipo == 'HH':
            # Validar y cambiar la hora
            if self.validarHora(valor):
                self.hora = valor + self.hora[2:5] + self.hora[5:]
            else:
                print("Hora inválida.")
        elif tipo == 'MM':
            # Validar y cambiar los minutos
            if self.validarMinutos(valor):
                self.hora = self.hora[:3] + valor + self.hora[5:]
            else:
                print("Minutos inválidos.")
        elif tipo == 'SS':
            # Validar y cambiar los segundos
            if self.validarSegundos(valor):
                self.hora = self.hora[:6] + valor
            else:
                print("Segundos inválidos.")
        else:
            print("Tipo de parámetro inválido.")

    def __str__(self):
        return f"{self.fecha} {self.hora}"

    def validarFormatoFecha

