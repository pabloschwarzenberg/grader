def shopping_cart(products):
  cart = {}
  for item in products.split(';'):
    if item.split(',')[0] in cart:
      cart[item.split(',')[0]] += int(item.split(',')[1])
    else:
      cart[item.split(',')[0]] = int(item.split(',')[1])
  return cart

def products_list(num):
  if num == 1:
    return 'Juego Pokemon X para Nintendo 3DS, 33.77'
  elif num == 2:
    return 'Nintendo 3DS XL, 203.00'
  elif num == 3:
    return 'Juego Mario Kart 7 para Nintendo 3DS, 27.58'
  elif num == 4:
    return 'PlayStation 4, 348.00'
  elif num == 5:
    return 'FIFA 16, PlayStation 4, 51.19'

def show_cart(cart, products):
  print('Productos en el carro:')
  for item
      