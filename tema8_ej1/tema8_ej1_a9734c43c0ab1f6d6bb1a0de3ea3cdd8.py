class Producto:
  def __init__(self,codigo,nombre,precio):
    self.codigo=codigo
    self.nombre=nombre
    self.precio=precio
    self.descuento=0

  def __str__(self):
    return "codigo="+str(self.codigo)+" "+self.nombre+" con precio="+str(self.precio)

  def __repr__(self):
    return str(self)

  def __eq__(self,other):
    if self.codigo==other.codigo:
      return True
    else:
      return False

  def precio_promocion(self):
    return self.precio-self.precio*self.descuento

p1=Producto(1,"Pokemon X",33.77)
p2=Producto(2,"Nintendo XL",203)
p3=Producto(3,"Mario Kart 7",27.58)
p4=Producto(4,"PlayStation 4",348.00)
p5=Producto(5,"FIFA 16",51.19)
productos=[p1,p2,p3,p4,p5]
#Imprimir todo como lista
print(productos)

#Imprimir cada producto
i=0
while i<len(productos):
  print(productos[i])
  i=i+1

p1.descuento=0.1
print(p1.precio_promocion())
print(p2.precio_promocion())

#Como ejercicio, completen el programa con la clase Carro y los métodos ver, checkout y agregarProducto

class Carro:
  def __init__(self):
    pass

  def ver(self):
    pass

  def checkout(self):
    pass

  def agregarProducto(self,producto,cantidad):
    pass
