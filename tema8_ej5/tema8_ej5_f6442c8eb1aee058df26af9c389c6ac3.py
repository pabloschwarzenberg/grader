class FechaHora:
    def __init__(self):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minuto = None
        self.segundo = None

    def fijarFecha(self, fecha):
        if fecha:
            if '/' in fecha:
                self.dia, self.mes, self.anio = fecha.split('/')
            elif '-' in fecha:
                self.dia, self.mes, self.anio = fecha.split('-')

            self.dia = int(self.dia)
            self.mes = int(self.mes)
            self.anio = int(self.anio)

    def fijarHora(self, hora):
        if hora:
            self.hora, self.minuto, self.segundo = hora.split(':')
            self.hora = int(self.hora)
            self.minuto = int(self.minuto)
            self.segundo = int(self.segundo)

    def fijarFechaHora(self, fecha_hora):
        if fecha_hora:
            fecha, hora = fecha_hora.split(' ')
            self.fijarFecha(fecha)
            self.fijarHora(hora)

    def cambiar(self, parametro):
        if parametro.startswith('dd='):
            nuevo_dia = int(parametro.split('=')[1])
            if self.validar_dia(nuevo_dia):
                self.dia = nuevo_dia
                print("Se ha cambiado el día correctamente.")
            else:
                print("Error: El día especificado es inválido.")
        elif parametro.startswith('mm='):
            nuevo_mes = int(parametro.split('=')[1])
            if self.validar_mes(nuevo_mes):
                self.mes = nuevo_mes
                print("Se ha cambiado el mes correctamente.")
            else:
                print("Error: El mes especificado es inválido.")
        elif parametro.startswith('aaaa='):
            nuevo_anio = int(parametro.split('=')[1])
            if self.validar_anio(nuevo_anio):
                self.anio = nuevo_anio
                print("Se ha cambiado el año correctamente.")
            else:
                print("Error: El año especificado es inválido.")
        elif parametro.startswith('HH='):
            nueva_hora = int(parametro.split('=')[1])
            if self.validar_hora(nueva_hora):
                self.hora = nueva_hora
                print("Se ha cambiado la hora correctamente.")
            else:
                print("Error: La hora especificada es inválida.")
        elif parametro.startswith('MM='):
            nuevo_minuto = int(parametro.split('=')[1])
            if self.validar_minuto(nuevo_minuto):
                self.minuto = nuevo_minuto
                print("Se ha cambiado el minuto correctamente.")
            else:
                print("Error: El minuto especificado es inválido.")
        elif parametro.startswith('SS='):
            nuevo_segundo = int(parametro.split('=')[1])
            if self.validar_segundo(nuevo_segundo):
                self.segundo = nuevo_segundo
                print("Se ha cambiado el segundo correctamente.")
            else:
                print("Error: El segundo especificado es inválido.")
        else:
            print("Error: Parámetro inválido.")

    def validar_dia(self, dia):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= dia <= 31
        elif self.mes in [4, 6, 9, 11]:
            return 1 <= dia <= 30
        elif self.mes == 2:
            if self.anio % 400 == 0 or (self.anio % 4 == 0 and self.anio % 100 != 0):
                return 1 <= dia <= 29
            else:
                return 1 <= dia <= 28
        else:
            return False

    def validar_mes(self, mes):
        return 1 <= mes <= 12

    def validar_anio(self, anio):
        return anio >= 0

    def validar_hora(self, hora):
        return 0 <= hora <= 23

    def validar_minuto(self, minuto):
        return 0 <= minuto <= 59

    def validar_segundo(self, segundo):
        return 0 <= segundo <= 59

    def __str__(self):
        fecha = f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d}"
        hora = f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
        return f"{fecha} {hora}"


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha('01/01/2023')
    fecha_hora.fijarHora('12:00:00')
    print(fecha_hora)

    fecha_hora.cambiar('dd=2')
    fecha_hora.cambiar('mm=13')
    fecha_hora.cambiar('aaaa=-2023')
    fecha_hora.cambiar('HH=24')
    fecha_hora.cambiar('MM=60')
    fecha_hora.cambiar('SS=70')
    print(fecha_hora)
