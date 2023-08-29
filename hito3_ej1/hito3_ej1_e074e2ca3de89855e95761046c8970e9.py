class Taxon:
  def __init__ (self, var1, var2):
    self.categoria = var1
    self.nombre = var2
  def Aves(self):
    print('El nombre del ave es', self.nombre, ', de la categoría ', {self.categoria})
    
     
if __name__ == "__main__":
    categoria = input('Ingrese la categoría: ')
    nombre = input('Ingrese el nombre: ')
    nombre_ave = Taxon(categoria,nombre)
    nombre_ave.Aves()


      