class Taxon():
  def __init__(self, nombre, categoria):
    self.nombre=nombre
    self.categoria=categoria
  def mostrar(self):
    print(self.nombre, self.categoria)
  def grabar(self):
    archivo=open("Nombre.txt", "a")
    variable=self.nombre+" "+self.categoria+"\n"
    archivo.write(variable)

nombre=input("Ingrese el nombre del ave: ")
categoria=input("Ingrese el nombre de la categoria: ")
clase_ave=Taxon(nombre,categoria)
clase_ave.grabar()      