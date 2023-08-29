class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

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
            'dd': 31, 'mm': 12, 'aaaa': 9999,
            'HH': 23, 'MM': 59, 'SS': 59
        }

        tipo_parametro, valor = parametro.split('=')
        tipo_parametro = tipo_parametro.strip().lower()
        valor = valor.strip()

        if tipo_parametro in parametros_validos:
            limite_superior = parametros_validos[tipo_parametro]
            if valor.isdigit() and 0 <= int(valor) <= limite_superior:
                if tipo_parametro == 'dd':
                    self.fecha = valor + self.fecha[2:5] + self.fecha[7:]
                elif tipo_parametro == 'mm':
                    self.fecha = self.fecha[:3] + valor + self.fecha[5:]
                elif tipo_parametro == 'aaaa':
                    self.fecha = self.fecha[:6] + valor
                elif tipo_parametro == 'hh':
                    self.hora = valor + self.hora[2:5] + self.hora[7:]
                elif tipo_parametro == 'mm':
                    self.hora = self.hora[:3] + valor + self.hora[5:]
                elif tipo_parametro == 'ss':
                    self.hora = self.hora[:6] + valor
            else:
                print("El valor ingresado para {} es inválido.".format(tipo_parametro))
        else:
            print("El parámetro ingresado no es válido.")

    def __str__(self):
        return "{}/{}/{} {}:{}:{}".format(self.fecha[6:], self.fecha[3:5], self.fecha[:2], self.hora[:2], self.hora[3:5], self.hora[6:])


# Ejemplo de uso
fecha_hora = FechaHora()

fecha_hora.fijarFecha('30/05/2015')
fecha_hora.fijarHora('17:45:00')
print(fecha_hora)  # Imprime: 2015/05/30 17:45:00

fecha_hora.fijarHora('18:00:00')
fecha_hora.cambiar('aaaa=2016')
print(fecha_hora)  # Imprime: 2016/05/30 18:00:00
