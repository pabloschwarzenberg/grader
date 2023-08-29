def bienvenida():
  print('Bienvenido a la tienda. Estos son los productos y valores: ')
  print(' ')
  print('1. Juego Pokemon X para Nintendo 3DS. Precio: USD 33.77')
  print('2. Nintendo 3DS XL. Precio: USD 203')
  print('3. Juego Mario Kart 7 para Nintendo 3DS. Precio: USD 27.58')
  print('4. PlayStation 4. Precio: USD 348.00')
  print('5. FIFA 16, PlayStation 4. Precio: USD 51.19')

def amazon(producto, unidades):
  global total_final
  total = 0
  
  if producto == 1:
    lista.append(1)
    print(' ')
    print('Has agregado al carro el producto 1. Juego Pokemon X para Nintendo 3DS')
    total += 33.77 * unidades    
    print('El precio es USD 33.77. Has seleccionado {unidades} unidades, por lo que el total es de: USD {total}')
    total_final += total

  elif producto == 2:
    lista.append(2)
    print(' ')
    print('Has agregado al carro el producto 2. Nintendo 3DS XL. Precio: USD 203')
    total += 203 * unidades
    print('El precio es USD 203. Has seleccionado {unidades} unidades, por lo que el total es de: USD {total}')
    total_final += total

  elif producto == 3:
    lista.append(3)
    print(' ')
    print('Has agregado al carro el producto 3. Juego Mario Kart 7 para Nintendo 3DS. Precio: USD 27.58')
    total += 27.58 * unidades
    print('El precio es USD 27.58. Has seleccionado {unidades} unidades, por lo que el total es de: USD {total}')
    total_final += total

  elif producto == 4:
    lista.append(4)
    print(' ')
    print('Has agregado al carro el producto 4. PlayStation 4. Precio: USD 348.00')
    total += 348 * unidades
    print('El precio es USD 348.00. Has seleccionado {unidades} unidades, por lo que el total es de: USD {total}')
    total_final += total

  elif producto == 5:
    lista.append(5)
    print(' ')
    print('Has agregado al carro el producto 5. FIFA 16, PlayStation 4. Precio: USD 51.19')
    total += 51.19 * unidades
    print('El precio es USD 51.19. Has seleccionado {unidades} unidades, por lo que el total es de: USD {total}')
    total_final += total


def tienda():
  global lista, total_final

  final = False
  total_final = 0
  lista = []

  print(' ')
  producto = int(input('Ingrese el número del producto que quiere agregar al carro: '))
  unidades = int(input('Ingrese la cantidad de unidades que quiere del producto seleccionado: '))

  amazon(producto, unidades)

  while final == False:
    print(' ')
    pregunta = input('¿Desea agregar otro producto? Responsa si/no: ')

    if pregunta == 'si':
      print(' ')
      producto = int(input('Ingrese el número del producto que quiere agregar al carro: '))
      unidades = int(input('Ingrese la cantidad de unidades que quiere del producto seleccionado: '))
      amazon(producto, unidades)

    elif pregunta == 'no':
      final = True

def cuenta_final():
  cuenta_final = 0
  
  if 1 and 2 and 3 in lista:
    cuenta_final = total_final * 0.8
    print(' ')
    print('La cuenta hasta ahora es de USD {total_final}')
    print('Por llevar los productos 1, 2 y 3, hay un 20% de descuento')

  if 4 and 5 in lista:
    cuenta_final = total_final * 0.85
    print(' ')
    print('La cuenta hasta ahora es de USD {total_final}')
    print('Por llevar los productos 4 y 5 hay un 15% de descuento')
  
  print('Por lo tanto el total, con los descuentos aplicados es de USD {cuenta_final}')

bienvenida()
tienda()
cuenta_final()