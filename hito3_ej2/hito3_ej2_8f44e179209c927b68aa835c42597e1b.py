class Taxon():
  def __init__(self, nombre, categoria):
    self.nombre=nombre
    self.categoria=categoria
    self.subcategoria=subcategoria
  def mostrar(self):
    print(self.nombre, self.categoria, self.subcategoria)
  def grabar(self):
    archivo=open("Nombre.txt", "a")
    variable=self.nombre+" "+self.categoria+"\n"
    archivo.write(variable)

nombre=input("Ingrese el nombre del ave: ")
categoria=input("Ingrese el nombre de la categoria: ")
subcategoria=input("Ingrese la subcategoria del ave: ")
clase_ave=Taxon(nombre,categoria)
clase_ave.mostrar()
clase_ave.grabar()