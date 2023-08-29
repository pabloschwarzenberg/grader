def fijarFecha(self, fecha_string):
    self.fecha = self._validarFecha(fecha_string)

def _validarFecha(self, fecha_string):
    try:
        dia, mes, anio = fecha_string.split('/')
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        if self._esFechaValida(dia, mes, anio):
            return dia, mes, anio
        else:
            print("Error: Fecha inválida.")
    except ValueError:
        print("Error: Formato de fecha inválido.")
