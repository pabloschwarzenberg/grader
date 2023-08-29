class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def fijarFecha(self, fecha_str):
        self.fecha = fecha_str

    def fijarHora(self, hora_str):
        self.hora = hora_str

    def fijarFechaHora(self, fecha_hora_str):
        fecha_hora = fecha_hora_str.split()
        self.fecha = fecha_hora[0]
        self.hora = fecha_hora[1]

    def cambiar(self, parametro):
        parametro = parametro.replace(" ", "")
        if "=" in parametro:
            key, value = parametro.split("=")
            if key == "dd":
                if not self.validar_dia(int(value)):
                    print("Día inválido.")
                    return
                self.fecha = self.actualizar_fecha("dia", int(value))
            elif key == "mm":
                if not self.validar_mes(int(value)):
                    print("Mes inválido.")
                    return
                self.fecha = self.actualizar_fecha("mes", int(value))
            elif key == "aaaa":
                if not self.validar_anio(int(value)):
                    print("Año inválido.")
                    return
                self.fecha = self.actualizar_fecha("anio", int(value))
            elif key == "HH":
                if not self.validar_hora(int(value)):
                    print("Hora inválida.")
                    return
                self.hora = self.actualizar_hora("hora", int(value))
            elif key == "MM":
                if not self.validar_minuto(int(value)):
                    print("Minuto inválido.")
                    return
                self.hora = self.actualizar_hora("minuto", int(value))
            elif key == "SS":
                if not self.validar_segundo(int(value)):
                    print("Segundo inválido.")
                    return
                self.hora = self.actualizar_hora("segundo", int(value))
            else:
                print("Parámetro inválido.")
        else:
            print("Formato de parámetro inválido.")

    def validar_dia(self, dia):
        return dia >= 1 and dia <= 31

    def validar_mes(self, mes):
        return mes >= 1 and mes <= 12

    def validar_anio(self, anio):
        return anio >= 0

    def validar_hora(self, hora):
        return hora >= 0 and hora <= 23

    def validar_minuto(self, minuto):
        return minuto >= 0 and minuto <= 59

    def validar_segundo(self, segundo):
        return segundo >= 0 and segundo <= 59

    def actualizar_fecha(self, tipo, valor):
        fecha_parts = self.fecha.split("/")
        dia = int(fecha_parts[0])
        mes = int(fecha_parts[1])
        anio = int(fecha_parts[2])

        if tipo == "dia":
            dia = valor
        elif tipo == "mes":
            mes = valor
        elif tipo == "anio":
            anio = valor

        return "{:02d}/{:02d}/{:04d}".format(dia, mes, anio)

    def actualizar_hora(self, tipo, valor):
        hora_parts = self.hora.split(":")
        hora = int(hora_parts[0])
        minuto = int(hora_parts[1])
        segundo = int(hora_parts[2])

        if tipo == "hora":
            hora = valor
        elif tipo == "minuto":
            minuto = valor
        elif tipo == "segundo":
            segundo = valor

        return "{:02d}:{:02d}:{:02d}".format(hora, minuto, segundo)

    def __repr__(self):
        return "{}/{} {}".format(self.fecha[6:], self.fecha[3:5], self.fecha[0:2], self.hora)
