class Taxon:
  def __init__(self, categoria, subcategorias, nombre):
    self.categoria = categoria
    grupo = subcategorias.split(" ")
    self.subcategorias = grupo
    self.nombre = nombre

pajaro = Taxon("feo", "gordo anomalo imbecil", "treile")
print(pajaro.categoria)
print(pajaro.subcategorias)
print(pajaro.nombre)
    