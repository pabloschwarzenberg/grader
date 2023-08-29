class Taxon:
  def __init__(self,categoria,nombre):
    self.categoria=categoria
    self.nombre=nombre
  def mostrar(self):
    print(self.categoria,self.nombre)
while True:
 a="pajaro"
 b="Guakamayo"
 ave=Taxon(a,b)
 ave.mostrar()
 break