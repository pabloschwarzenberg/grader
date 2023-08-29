class Taxon:
  def __init__ (self, var1, var2, var3=[]):
    self.categoria = var1
    self.nombre = var2
    self.subcategoria = var3
  def Aves(self):
    print('El nombre del ave es', self.nombre, ', de la categoría ', self.categoria, 'de la subcategoria', self.subcategoria)
    

if __name__ == "__main__":
    nombre = input('Ingrese el nombre: ')
    categoria = input('Ingrese la categoría: ')
    subcategoria = [input('Ingrese la subcategoria: ')]

    nombre_ave = Taxon(categoria,nombre, subcategoria)
    nombre_ave.Aves()