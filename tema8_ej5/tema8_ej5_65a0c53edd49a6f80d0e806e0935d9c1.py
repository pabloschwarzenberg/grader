class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        if "/" in fecha_str:
            formato = "%d/%m/%Y"
        elif "-" in fecha_str:
            formato = "%d-%m-%Y"
        else:
            print("Formato de fecha inválido. Utilice dd/mm/aaaa o dd-mm-aaaa.")
            return
        from datetime import datetime
        try:
            fecha_obj = datetime.strptime(fecha_str, formato)
            self.fecha = fecha_obj.date()
        except ValueError:
            print("Fecha inválida. Introduzca una fecha válida en formato dd/mm/aaaa o dd-mm-aaaa.")

    def fijarHora(self, hora_str):
        formato = "%H:%M:%S"
        from datetime import datetime
        try:
            hora_obj = datetime.strptime(hora_str, formato)
            self.hora = hora_obj.time()
        except ValueError:
            print("Hora inválida. Introduzca una hora válida en formato HH:MM:SS.")

    def fijarFechaHora(self, fecha_hora_str):
        if "/" in fecha_hora_str:
            formato = "%d/%m/%Y %H:%M:%S"
        elif "-" in fecha_hora_str:
            formato = "%d-%m-%Y %H:%M:%S"
        else:
            print("Formato de fecha y hora inválido. Utilice dd/mm/aaaa HH:MM:SS o dd-mm-aaaa HH:MM:SS.")
            return
        from datetime import datetime
        try:
            fecha_hora_obj = datetime.strptime(fecha_hora_str, formato)
            self.fecha = fecha_hora_obj.date()
            self.hora = fecha_hora_obj.time()
        except ValueError:
            print("Fecha y hora inválidas. Introduzca una fecha y hora válidas en formato dd/mm/aaaa HH:MM:SS o dd-mm-aaaa HH:MM:SS.")

    def cambiar(self, parametro):
        if "=" not in parametro:
            print("Formato de parámetro inválido. Utilice 'dd=valor', 'mm=valor', 'aaaa=valor', 'HH=valor', 'MM=valor' o 'SS=valor'.")
            return
        tipo, valor = parametro.split("=")
        tipo = tipo.strip()
        valor = valor.strip()
        if tipo == "dd":
            valor = int(valor)
            if valor < 1 or valor > 31:
                print("Valor de día inválido. Debe ser un número entre 1 y 31.")
                return
        elif tipo == "mm":
            valor = int(valor)
            if valor < 1 or valor > 12:
                print("Valor de mes inválido. Debe ser un número entre 1 y 12.")
                return
        elif tipo == "aaaa":
            valor = int(valor)
            if valor < 1:
                print("Valor de año inválido. Debe ser un número positivo.")
                return
        elif tipo == "HH":
            valor = int(valor)
            if valor < 0 or valor > 23:
                print("Valor de hora inválido. Debe ser un número entre 0 y 23.")
                return
        elif tipo == "MM" or tipo == "SS":
            valor = int(valor)
            if valor < 0 or valor > 59:
                print("Valor de minutos o segundos inválido. Debe ser un número entre 0 y 59.")
                return
        else:
            print("Tipo de parámetro inválido. Utilice 'dd', 'mm', 'aaaa', 'HH', 'MM' o 'SS'.")
            return
        if self.fecha is not None and self.hora is not None:
            from datetime import datetime
            fecha_hora_obj = datetime.combine(self.fecha, self.hora)
            if tipo == "dd":
                fecha_hora_obj = fecha_hora_obj.replace(day=valor)
            elif tipo == "mm":
                fecha_hora_obj = fecha_hora_obj.replace(month=valor)
            elif tipo == "aaaa":
                fecha_hora_obj = fecha_hora_obj.replace(year=valor)
            elif tipo == "HH":
                fecha_hora_obj = fecha_hora_obj.replace(hour=valor)
            elif tipo == "MM":
                fecha_hora_obj = fecha_hora_obj.replace(minute=valor)
            elif tipo == "SS":
                fecha_hora_obj = fecha_hora_obj.replace(second=valor)
            self.fecha = fecha_hora_obj.date()
            self.hora = fecha_hora_obj.time()

    def __str__(self):
        if self.fecha is not None and self.hora is not None:
            cadena = self.fecha.strftime("%Y/%m/%d") + " " + self.hora.strftime("%H:%M:%S")
            return cadena
        else:
            return "Fecha y hora no establecidas"