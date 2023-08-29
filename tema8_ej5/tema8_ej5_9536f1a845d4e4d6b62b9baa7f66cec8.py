class FechaHora:
class FechaHora:
    def __init__(self, fecha='', hora=''):
        self.fijarFechaHora(fecha, hora)

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha, hora):
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        parametro = parametro.replace(' ', '')
        partes = parametro.split('=')
        if len(partes) != 2:
            print('Error: formato de parámetro inválido.')
            return

        tipo = partes[0].lower()
        valor = partes[1]

        if tipo == 'dd':
            if not self.esDiaValido(valor):
                print('Error: día inválido.')
                return
            self.fecha = valor + self.fecha[2:]
        elif tipo == 'mm':
            if not self.esMesValido(valor):
                print('Error: mes inválido.')
                return
            self.fecha = self.fecha[:3] + valor + self.fecha[5:]

        elif tipo == 'aaaa':
            if not self.esAnioValido(valor):
                print('Error: año inválido.')
                return
            self.fecha = self.fecha[:6] + valor

        elif tipo == 'hh':
            if not self.esHoraValida(valor):
                print('Error: hora inválida.')
                return
            self.hora = valor + self.hora[2:]

        elif tipo == 'mm':
            if not self.esMinutoValido(valor):
                print('Error: minuto inválido.')
                return
            self.hora = self.hora[:3] + valor + self.hora[5:]

        elif tipo == 'ss':
            if not self.esSegundoValido(valor):
                print('Error: segundo inválido.')
                return
            self.hora = self.hora[:6] + valor

        else:
            print('Error: parámetro desconocido.')

    def esDiaValido(self, dia):
        return dia.isdigit() and 1 <= int(dia) <= 31

    def esMesValido(self, mes):
        return mes.isdigit() and 1 <= int(mes) <= 12

    def esAnioValido(self, anio):
        return anio.isdigit() and len(anio) == 4

    def esHoraValida(self, hora):
        return hora.isdigit() and 0 <= int(hora) <= 23

    def esMinutoValido(self, minuto):
        return minuto.isdigit() and 0 <= int(minuto) <= 59

    def esSegundoValido(self, segundo):
        return segundo.isdigit() and 0 <= int(segundo) <= 59

    def __str__(self):
        return f'{self.fecha} {self.hora}'


# Ejemplo de uso
fecha_hora = FechaHora()
print(fecha_hora)  # Salida:  / 00:00:00

fecha_hora.fijarFecha('20/06/2023')
fecha_hora.fijarHora('09:30:00')
print(fecha_hora)  # Salida: 2023/06/20 09:30:00

fecha_hora.cambiar('dd=30')
fecha_hora.cambiar('mm=12')
fecha_hora.cambiar('aaaa=2022')
fecha_hora.cambiar
