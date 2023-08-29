p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

def carrito(producto,cantidad):
  carrito = []
  cantidad = int(cantidad)
  if producto == 1:
    for i in range(cantidad):
      carrito.append(p1)
  elif producto == 2:
    for i in range(cantidad):
      carrito.append(p2)
  if producto == 3:
    for i in range(cantidad):
      carrito.append(p3)
  if producto == 4:
    for i in range(cantidad):
      carrito.append(p4)
  else:
    for i in range(cantidad):
      carrito.append(p5)
  return carrito

def mostrar(lista):
  for i in lista:
    print('-',i)

def total(lista):
  total = 0
  for i in lista:
    total = total + i[2]
  return total

n = input('producto: ')
x = input('que desea hacer?: ')
a = n[0]
b= n[2]
lista = carrito(a,b)
if x == 'ver':
  ver = mostrar(lista)
  print(ver)
elif x == 'checkout':
  total = total(lista)
  print(total)