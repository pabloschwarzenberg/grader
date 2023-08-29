class FechaHora:
    def __init__(self, fecha, hora):
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def fijarFecha(self, fecha):
        separador = '/' if '/' in fecha else '-'
        dia, mes, anio = fecha.split(separador)
        self.dia = int(dia)
        self.mes = int(mes)
        self.anio = int(anio)

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        if '=' not in parametro:
            print("Error: El formato del parámetro es incorrecto.")
            return

        clave, valor = parametro.split('=')
        clave = clave.strip().lower()
        valor = valor.strip()

        if clave == 'dd':
            dia = int(valor)
            if dia < 1 or dia > 31:
                print("Error: El valor del día es inválido.")
            else:
                self.dia = dia
        elif clave == 'mm':
            mes = int(valor)
            if mes < 1 or mes > 12:
                print("Error: El valor del mes es inválido.")
            else:
                self.mes = mes
        elif clave == 'aaaa':
            anio = int(valor)
            if anio < 1:
                print("Error: El valor del año es inválido.")
            else:
                self.anio = anio
        elif clave == 'hh':
            hora = int(valor)
            if hora < 0 or hora > 23:
                print("Error: El valor de la hora es inválido.")
            else:
                self.hora = hora
        elif clave == 'mm':
            minuto = int(valor)
            if minuto < 0 or minuto > 59:
                print("Error: El valor del minuto es inválido.")
            else:
                self.minuto = minuto
        elif clave == 'ss':
            segundo = int(valor)
            if segundo < 0 or segundo > 59:
                print("Error: El valor del segundo es inválido.")
            else:
                self.segundo = segundo
        else:
            print("Error: El parámetro especificado no es válido.")

    def __repr__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

           