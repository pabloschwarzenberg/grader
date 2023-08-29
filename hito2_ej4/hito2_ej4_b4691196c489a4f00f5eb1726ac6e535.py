class CarroDeCompras:
  
  def __init__(self):
    self.productos = {}
    
  def agregar_producto(self, producto, cantidad):
    if producto in self.productos:
      self.productos[producto] += cantidad
    else:
      self.productos[producto] = cantidad
    print("Se agregaron", cantidad, "unidades del producto", producto)
    
  def ver_carro(self):
    if not self.productos:
      print("El carro está vacío.")
    else:
      print("Productos en el carro:")
      for producto, cantidad in self.productos.items():
        print(producto, "-", cantidad)
    
  def checkout(self):
    total = 0
    for producto, cantidad in self.productos.items():
      if producto == 1:
        total += cantidad * 33.77
      elif producto == 2:
        total += cantidad * 203
      elif producto == 3:
        total += cantidad * 27.58
      elif producto == 4:
        total += cantidad * 348
      elif producto == 5:
        total += cantidad * 51.19
    if 1 in self.productos and 2 in self.productos and 3 in self.productos:
      total *= 0.8
    elif 4 in self.productos and 5 in self.productos:
      total *= 0.85
    print("Total a pagar: $", round(total, 1))
    
carro = CarroDeCompras()
while True:
  orden = input("Ingrese la orden (Agregar producto: 'producto,cantidad', Ver carro: 'ver', Checkout: 'checkout'): ")
  if orden == "ver":
    carro.ver_carro()
  elif orden == "checkout":
    carro.checkout()
    break
  else:
    orden = orden.split(",")
    producto = int(orden[0])
    cantidad = int(orden[1])
    carro.agregar_producto(producto, cantidad)
