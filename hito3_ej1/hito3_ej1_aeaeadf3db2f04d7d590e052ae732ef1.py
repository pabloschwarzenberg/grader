class Taxon:
  def __init__(self,categoria,nombre):
      registro = []
      self.categoria = categoria
      self.nombre = nombre
  def registro(self):
    registro = []
    p = True
    while p == True:
      registro.append(self.nombre)
      registro.append(self.categoria)
      p = False
    return registro

      