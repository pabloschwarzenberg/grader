class FechaHora:
    def __init__(self, fecha=None, hora=None):
        self.fecha = fecha
        self.hora = hora

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        parametros_validos = {
            'dd': self.cambiarDia,
            'mm': self.cambiarMes,
            'aaaa': self.cambiarAnio,
            'HH': self.cambiarHora,
            'MM': self.cambiarMinuto,
            'SS': self.cambiarSegundo
        }

        try:
            parametro, valor = parametro.split('=')
            parametro = parametro.strip()
            valor = valor.strip()

            if parametro in parametros_validos:
                parametros_validos[parametro](valor)
            else:
                print("Parámetro inválido.")
        except ValueError:
            print("Formato de parámetro inválido.")

    def cambiarDia(self, dia):
        if not dia.isdigit():
            print("El día debe ser un número entero.")
            return

        dia = int(dia)

        if dia < 1 or dia > 31:
            print("Día inválido.")
            return

        self.fecha = self.fecha[:2] + str(dia) + self.fecha[2:]

    def cambiarMes(self, mes):
        if not mes.isdigit():
            print("El mes debe ser un número entero.")
            return

        mes = int(mes)

        if mes < 1 or mes > 12:
            print("Mes inválido.")
            return

        self.fecha = self.fecha[:5] + str(mes) + self.fecha[6:]

    def cambiarAnio(self, anio):
        if not anio.isdigit():
            print("El año debe ser un número entero.")
            return

        anio = int(anio)

        if anio < 1:
            print("Año inválido.")
            return

        self.fecha = str(anio) + self.fecha[4:]

    def cambiarHora(self, hora):
        if not hora.isdigit():
            print("La hora debe ser un número entero.")
            return

        hora = int(hora)

        if hora < 0 or hora > 23:
            print("Hora inválida.")
            return

        self.hora = str(hora) + self.hora[2:]

    def cambiarMinuto(self, minuto):
        if not minuto.isdigit():
            print("El minuto debe ser un número entero.")
            return

        minuto = int(minuto)

        if minuto < 0 or minuto > 59:
            print("Minuto inválido.")
            return

        self.hora = self.hora[:3] + str(minuto) + self.hora[5:]

    def cambiarSegundo(self, segundo):
        if not segundo.isdigit():
            print("El segundo debe ser un número entero.")
            return
            
        segundo = int(segundo)

        if segundo <= 0 or segundo >= 59:
            print("Segundo inválido.")
            return

        self.hora = self.hora[:6] + str(segundo)

    def __repr__(self):
        return f"Fecha: {self.fecha}, Hora: {self.hora}"

    def __str__(self):
        return f"{self.fecha} {self.hora}"
