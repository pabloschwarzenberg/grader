class Taxon:
  def __init__(self, categoria, nombre):
    self.categoria = categoria
    self.nombre = nombre
    self.subcategorias = []
    
  def incluir(self, subcategoria):
    self.subcategorias.append(subcategoria)
    
tx = Taxon("cccc", "nnnn")

tx.incluir("scscsc")
print(tx.subcategorias)