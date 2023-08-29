class Taxon:
     categoria_ave = 0
     nombre_ave = 0
  def __init__(self, categoria_ave, nombre_ave)
     self.categoria_ave = categoria_ave
     self.nombre_ave = nombre_ave
nombre_archivo = str(input("ingrese nombre del archivo "))
lista_productos = []
f = open(nombre_archivo, "r")
linea = f.readlines()
for elemento in linea:
    elemento_separado = elemento.split(";")
    a = taxon(elemento_separado[0], elemento_separado[1])
    print(a)
	pass
      