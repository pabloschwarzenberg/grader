Para crear una clase en Python que maneje fechas y horas con métodos, puedes utilizar el módulo datetime que proporciona clases para manipular fechas y horas1.

Para fijar la fecha y la hora, puedes utilizar los métodos datetime.date() y datetime.time() respectivamente2. Para fijar la fecha y hora juntos, puedes utilizar el método datetime.datetime()2.

Para cambiar cualquier parámetro (día, hora, etc.) con un método cambiar que reciba como argumento un string que especifica el tipo de parámetro y su valor, el cual se debe validar. Por ejemplo, si quieres cambiar el día a 2, deberías usar como parámetro ’dd=2’, sin importar los espacios3.

Para mostrar un objeto de la clase FechaHora mediante print con la fecha en formato aaaa/mm/dd HH:MM:SS, puedes utilizar el método strftime()21.

Aquí te dejo un ejemplo de cómo podrías crear la clase:

import datetime

class FechaHora:
    def __init__(self):
        self.fecha = datetime.date.today()
        self.hora = datetime.datetime.now().time()

    def fijarFecha(self, fecha):
        self.fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y').date()

    def fijarHora(self, hora):
        self.hora = datetime.datetime.strptime(hora, '%H:%M:%S').time()

    def fijarFechaHora(self, fecha_hora):
        self.fecha, self.hora = datetime.datetime.strptime(fecha_hora, '%d/%m/%Y %H:%M:%S').date(), datetime.datetime.strptime(fecha_hora, '%d/%m/%Y %H:%M:%S').time()

    def cambiar(self, parametro):
        parametro = parametro.replace(" ", "")
        parametro = parametro.split("=")
        if parametro[0] == "dd":
            if int(parametro[1]) > 31:
                print("El día no puede ser mayor a 31")
            else:
                self.fecha = self.fecha.replace(day=int(parametro[1]))
        elif parametro[0] == "mm":
            if int(parametro[1]) > 12:
                print("El mes no puede ser mayor a 12")
            else:
                self.fecha = self.fecha.replace(month=int(parametro[1]))
        elif parametro[0] == "aaaa":
            if int(parametro[1]) < 1900:
                print("El año no puede ser menor a 1900")
            else:
                self.fecha = self.fecha.replace(year=int(parametro[1]))
        elif parametro[0] == "HH":
            if int(parametro[1]) > 23:
                print("La hora no puede ser mayor a 23")
            else:
                self.hora = self.hora.replace(hour=int(parametro[1]))
        elif parametro[0] == "MM":
            if int(parametro[1]) > 59:
                print("Los minutos no pueden ser mayores a 59")
            else:
                self.hora = self.hora.replace(minute=int(parametro[1]))
        elif parametro[0] == "SS":
            if int(parametro[1]) > 59:
                print("Los segundos no pueden ser mayores a 59")
            else:
                self.hora = self.hora.replace(second=int(parametro[1]))

    def __str__(self):
        return str(self.fecha.strftime('%Y/%m/%d')) + ' ' + str(self.hora.strftime('%H:%M:%S'))

fecha_hora = FechaHora()
fecha_hora.fijarFecha('19/06/2023')
fecha_hora.fijarHora('12:19:04')
print(fecha_hora)