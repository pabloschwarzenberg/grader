class Taxon:
  def __init__(self,categoria,nombre, subcategorias):
      self.categoria = categoria
      self.nombre = nombre
      self.subcategorias = subcategorias
  def registro(self):
    registro = []
    p = True
    while p == True:
      registro.append(self.nombre)
      registro.append(self.categoria)
      p = False
    return registro
  def grupo(self):
    grupos = []
    for lista in range(1):
      grupos.append(self.subcategorias)
      for i in range(1):
        grupos.append(registro)
    return grupos
      