class Carro_De_Compras:
 def __init__(self):
  self.productos=[]
  self.discount=0
  self.total=0
  self.direccion=""

 def Agregar_Producto(self, cuantos, producto):
  for item in self.productos:
   if item.producto==producto:
    if cuantos==0: 
     self.productos.remove(item) 
    else: 
     item.cuantos=cuantos 
    return 
  item=Objeto(cuantos, producto)
  self.productos.append(item)

 def Checkout(self, tipoDespacho, direccion):
  subtotal=sum(item.producto.costo * item.cuantos for item in self.productos)
  descuento=0
  if len(self.productos)>=3 and all(item.producto.item_id in [1, 2, 3] for item in self.productos):
   descuento=subtotal * 0.2
  elif len(self.productos)>=2 and all(item.producto.item_id in [4, 5] for item in self.productos):
   descuento=subtotal * 0.15
  despacho=0
  if tipoDespacho==0: 
   despacho=(subtotal-descuento)*0.2
  elif tipoDespacho==1: 
   despacho=(subtotal - descuento)*0.3
  total=subtotal-descuento+despacho
  if "chile" in direccion.lower():
   total*=1.2
  return round(total, 0)

 def __repr__(self):
  s="Carro de Compras:\n"
  for item in self.productos:
   s=s+"{0}: {1}\n".format(item.cuantos, item.producto.id)
  return s
  
class Producto:
 def __init__(self, item_id, id, stock, costo):
  self.item_id=item_id
  self.stock=stock
  self.costo=costo
  self.id=id

 def __eq__(self, other):
  if self.item_id==other.item_id:
   return True
  else:
   return False

class Objeto:
 def __init__(self, cuantos, producto):
  self.cuantos=cuantos
  self.producto=producto

class Tienda:
 def __init__(self):
  self.menu_tienda=[]
  producto=Producto(1, "Juego Pokemon Y", 10, 31.51)
  self.menu_tienda.append(producto)
  producto=Producto(2, "Nintendo 3DS", 5, 190.95)
  self.menu_tienda.append(producto)
  producto=Producto(3, "Juego Mario Kart", 10, 29.96)
  self.menu_tienda.append(producto)
  producto=Producto(4, "Playstation 4", 10, 399)
  self.menu_tienda.append(producto)
  producto=Producto(5, "Fifa 14", 10, 41.95)
  self.menu_tienda.append(producto)

 def Menu(self):
  for producto in self.menu_tienda:
   print("{0}: {1} ${2}".format(producto.item_id, producto.id, producto.costo))

 def Carro(self, numero):
  for producto in self.menu_tienda:
   if producto.item_id==numero:
    return producto

if __name__=="__main__":
 tienda=Tienda()
 carro=Carro_De_Compras()
 while (1):
  tienda.Menu()
  producto_en_carro=input("Que quieres comprar? ID,Cantidad: ")
  if producto_en_carro=="":
   break
  else:
   producto_en_carro=producto_en_carro.split(",")
   numero=int(producto_en_carro[0])
   producto=tienda.Carro(numero)
   cuantos=int(producto_en_carro[1])
   carro.Agregar_Producto(cuantos, producto)
  print(carro)
 print(carro.Checkout(0, "usa"))
 print(carro.Checkout(1, "usa"))
 print(carro.Checkout(0, "Alameda 340 Santiago Chile"))
 print(carro.Checkout(1, "Alameda 340 Santiago Chile"))