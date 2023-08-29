p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]


orden = None

carrito = []


print("Bienvenid@ a la tienda.")
print("Opciones:")
print("ver: muestra el carrito")
print("checkout: realiza la compra")
print("O bien introduzca producto,cantidad")


while orden != 'checkout':
  orden = input("\nIntroduzca orden:")

  if orden == 'ver':
    for producto, cantidad in carrito:
        print(cantidad + " " + eval("p" + producto + "[1]"))

  elif orden == 'checkout':
    precio = 0
    productos = []
    for producto, cantidad in carrito:
      precio += float(eval('p' + producto + '[2]')) * int(cantidad)
      productos.append(producto)

   
    if '1' in productos and '2' in productos and '3' in productos:
      precio -= precio * 20 / 100
    elif '4' in productos and '5' in productos:
      precio -= precio * 15 / 100

    print(round(precio, 1))
  
  else:
    producto, cantidad = orden.split(',')
    
    conjunto = (producto, cantidad)
    carrito.append(conjunto)
  
