class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minutos = 0
        self.segundos = 0
    
    def fijarFecha(self, fecha):
        partes = fecha.split('/')
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])
    
    def fijarHora(self, hora):
        partes = hora.split(':')
        self.hora = int(partes[0])
        self.minutos = int(partes[1])
        self.segundos = int(partes[2])
    
    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(' ')
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])
    
    def cambiar(self, parametro):
        partes = parametro.split('=')
        tipo = partes[0].strip()
        valor = partes[1].strip()
        
        if tipo == 'dd':
            dia = int(valor)
            if dia >= 1 and dia <= 31:
                self.dia = dia
            else:
                print('Error: Día inválido')
        elif tipo == 'mm':
            mes = int(valor)
            if mes >= 1 and mes <= 12:
                self.mes = mes
            else:
                print('Error: Mes inválido')
        elif tipo == 'aaaa':
            anio = int(valor)
            if anio >= 1900:
                self.anio = anio
            else:
                print('Error: Año inválido')
        elif tipo == 'HH':
            hora = int(valor)
            if hora >= 0 and hora <= 23:
                self.hora = hora
            else:
                print('Error: Hora inválida')
        elif tipo == 'MM':
            minutos = int(valor)
            if minutos >= 0 and minutos <= 59:
                self.minutos = minutos
            else:
                print('Error: Minutos inválidos')
        elif tipo == 'SS':
            segundos = int(valor)
            if segundos >= 0 and segundos <= 59:
                self.segundos = segundos
            else:
                print('Error: Segundos inválidos')
        else:
            print('Error: Parámetro inválido')
    
    def __str__(self):
        fecha_str = f"{self.anio}/{self.mes:02d}/{self.dia:02d}"
        hora_str = f"{self.hora:02d}:{self.minutos:02d}:{self.segundos:02d}"
        return f"{fecha_str} {hora_str}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha('25/06/2022')
fecha_hora.fijarHora('08:30:00')
print(fecha_hora)  # Imprime: 2022/06/25 08:30:00

fecha_hora.cambiar('dd=12')
fecha_hora.cambiar('mm=11')
fecha_hora.cambiar('aaaa=2023')
fecha_hora.cambiar('HH=15')
fecha_hora.cambiar('MM=45')
fecha_hora.cambiar('SS=30')
print(fecha_hora)  # Imprime: 2023/11/12 15:45:30
