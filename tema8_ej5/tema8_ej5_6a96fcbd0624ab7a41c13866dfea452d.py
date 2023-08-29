class FechaHora:
  def __init__(self):
    self.dia = "01"
    self.mes = "01"
    self.ano = "1990"
    self.hora = 0
    self.minuto = 0
    self.segundo = 0
  
  def fijarFecha(self, fecha):
    self.dia = fecha[0:2]
    self.mes = fecha[3:5]
    self.ano = fecha[6:10]
    
  def fijarHora(self, hora):
    self.hora = hora[0:2]
    self.minuto = hora[3:5]
    self.seguno = hora[6:8]
  
  def fijarFechaHora(self, fechahora):
    fecha, hora = fechahora.split()
    self.fijarFecha(fecha)
    self.fijarHora(hora)
    
  def cambiar(self, value):
    seleccion, valor = value.split("=")
    
    if seleccion == "dd":
      self.dia = value
    if seleccion == "mm":
      self.mes = value
    if seleccion == "aaaa":
      self.ano = value
    if seleccion == "HH":
      self.hora = value
    if seleccion == "MM":
      self.minuto = value
    if seleccion == "SS":
      self.segundo = value
  
  def __str__(self):
    return (str(self.ano) + "/" + str(self.mes) + "/" + str(self.dia) + " " + str(self.hora) + ":" + str(self.minuto) + ":" + str(self.segundo))