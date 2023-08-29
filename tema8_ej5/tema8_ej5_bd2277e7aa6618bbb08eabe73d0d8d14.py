class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def fijarFecha(self, fecha_str):
        self.fecha = fecha_str

    def fijarHora(self, hora_str):
        self.hora = hora_str

    def fijarFechaHora(self, fecha_hora_str):
        fecha_hora = fecha_hora_str.split(' ')
        self.fecha = fecha_hora[0]
        self.hora = fecha_hora[1]

    def cambiar(self, parametro):
        param = parametro.split('=')
        if len(param) != 2:
            print("Formato de parámetro incorrecto. Debe ser 'tipo=valor'.")
            return

        tipo = param[0].strip()
        valor = param[1].strip()

        if tipo == "dd":
            if not self._validar_dia(valor):
                print("Día inválido.")
                return
            self.fecha = self._reemplazar_componente_fecha(self.fecha, 0, valor)
        elif tipo == "mm":
            if not self._validar_mes(valor):
                print("Mes inválido.")
                return
            self.fecha = self._reemplazar_componente_fecha(self.fecha, 1, valor)
        elif tipo == "aaaa":
            if not self._validar_anio(valor):
                print("Año inválido.")
                return
            self.fecha = self._reemplazar_componente_fecha(self.fecha, 2, valor)
        elif tipo == "HH":
            if not self._validar_hora(valor):
                print("Hora inválida.")
                return
            self.hora = self._reemplazar_componente_hora(self.hora, 0, valor)
        elif tipo == "MM":
            if not self._validar_minuto(valor):
                print("Minuto inválido.")
                return
            self.hora = self._reemplazar_componente_hora(self.hora, 1, valor)
        elif tipo == "SS":
            if not self._validar_segundo(valor):
                print("Segundo inválido.")
                return
            self.hora = self._reemplazar_componente_hora(self.hora, 2, valor)
        else:
            print("Tipo de parámetro no válido.")

    def _validar_dia(self, dia):
        try:
            dia_int = int(dia)
            if dia_int < 1 or dia_int > 31:
                return False
            return True
        except ValueError:
            return False

    def _validar_mes(self, mes):
        try:
            mes_int = int(mes)
            if mes_int < 1 or mes_int > 12:
                return False
            return True
        except ValueError:
            return False

    def _validar_anio(self, anio):
        try:
            anio_int = int(anio)
            if anio_int < 0:
                return False
            return True
        except ValueError:
            return False

    def _validar_hora(self, hora):
        try:
            hora_int = int(hora)
            if hora_int < 0 or hora_int > 23:
                return False
            return True
        except ValueError:
            return False

    def _validar_minuto(self, minuto):
        try:
            minuto_int = int(minuto)
            if minuto_int < 0 or minuto_int > 59:
               

        
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           