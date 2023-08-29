class FechaHora:
  def __init__(self):
    self.dia = 1
    self.mes = 1
    self.anio = 1900
    self.hora = 0
    self.minuto = 0
    self.segundo = 0
    
  def fijarFecha(self, fecha):
    if '/' in fecha:
      self.dia, self.mes, self.anio = fecha.split('/')
    elif '-' in fecha:
      self.dia, self.mes, self.anio = fecha.split('-')
    else:
      print('Formato de fecha incorrecto')

  def fijarHora(self, hora):
    self.hora, self.minuto, self.segundo = hora.split(':')

  def fijarFechaHora(self, fechahora):
    self.fijarFecha(fechahora[:10])
    self.fijarHora(fechahora[11:])

  def cambiar(self, parametro):
    parametro = parametro.replace(' ', '')
    tipo, valor = parametro.split('=')
    if tipo == 'dd':
      if int(valor) > 31:
        print('Día incorrecto')
      else:
        self.dia = int(valor)
    elif tipo == 'mm':
      if int(valor) > 12:
        print('Mes incorrecto')
      else:
        self.mes = int(valor)
    elif tipo == 'aaaa':
      self.anio = int(valor)
    elif tipo == 'HH':
      if int(valor) > 23:
        print('Hora incorrecta')
      else:
        self.hora = int(valor)
    elif tipo == 'MM':
      if int(valor) > 59:
        print('Minuto incorrecto')
      else:
        self.minuto = int(valor)
    elif tipo == 'SS':
      if int(valor) > 59:
        print('Segundo incorrecto')
      else:
        self.segundo = int(valor)
    else:
      print('Tipo de parámetro incorrecto')
        
  def __str__(self):
    return '{}/{}/{} {}:{}:{}'.format(self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo)
