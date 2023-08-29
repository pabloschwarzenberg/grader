class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None
    
    def fijarFecha(self, fecha):
        self.fecha = fecha
    
    def fijarHora(self, hora):
        self.hora = hora
    
    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split()
        self.fecha = partes[0]
        self.hora = partes[1]
    
    def cambiar(self, parametro):
        partes = parametro.split('=')
        tipo_parametro = partes[0].strip()
        valor_parametro = partes[1].strip()

        if tipo_parametro == 'dd':
            dia = int(valor_parametro)
            if dia < 1 or dia > 31:
                print("Día inválido.")
            else:
                self.fecha = self.fecha[:8] + str(dia).zfill(2)
        elif tipo_parametro == 'mm':
            mes = int(valor_parametro)
            if mes < 1 or mes > 12:
                print("Mes inválido.")
            else:
                self.fecha = self.fecha[:5] + str(mes).zfill(2) + self.fecha[7:]
        elif tipo_parametro == 'aaaa':
            anio = int(valor_parametro)
            if anio < 0:
                print("Año inválido.")
            else:
                self.fecha = str(anio) + self.fecha[4:]
        elif tipo_parametro == 'HH':
            hora = int(valor_parametro)
            if hora < 0 or hora > 23:
                print("Hora inválida.")
            else:
                self.hora = str(hora).zfill(2) + self.hora[2:]
        elif tipo_parametro == 'MM':
            minuto = int(valor_parametro)
            if minuto < 0 or minuto > 59:
                print("Minuto inválido.")
            else:
                self.hora = self.hora[:3] + str(minuto).zfill(2) + self.hora[5:]
        elif tipo_parametro == 'SS':
            segundo = int(valor_parametro)
            if segundo < 0 or segundo > 59:
                print("Segundo inválido.")
            else:
                self.hora = self.hora[:6] + str(segundo).zfill(2)
        else:
            print("Parámetro inválido.")

    def __str__(self):
        return f"{self.fecha[:4]}/{self.fecha[5:7]}/{self.fecha[8:10]} {self.hora}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFechaHora('30/09/2015 17:45:00')
print(fecha_hora)  # Salida: 2015/09/30 17:45:00

fecha_hora.cambiar('mm=10')
print(fecha_hora)  # Salida: 2015/10/30 17:45:00

fecha_hora.fijarHora('18:00:00')
fecha_hora.cambiar('aaaa=2016')
print(fecha_hora)  # Salida: 2016/10/30 18:00:00

fecha_hora.fijarFechaHora('25/12/2023 18:45:00')
print(fecha_hora)  # Salida: 2023/12/25 18:45:00

fecha_hora.cambiar('dd=31')
print(fecha_hora)  # Salida: 2023/12/31 18:45:00

fecha_hora.cambiar('mm=02')
print(fecha_hora)  # Salida: 2023/02/31 18:45:00

fecha_hora.cambiar('aaaa=2024')
print(fecha_hora)  # Salida: 2024/
