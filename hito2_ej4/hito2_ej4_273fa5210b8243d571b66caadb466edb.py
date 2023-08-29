p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro = []
catalogo = [p1, p2, p3, p4, p5]

def agregarcarro(s):
  global carro
  repite = False

  for lista in carro:
      if lista[0] == int(s[0]):
            repite = True
            lista[1] = int(lista[1]) + int(s[2])

  if 0 < int(s[0]) < 6 and len(s) > 2 and repite == False:
        producto = int(s[0])
        cantidad = int(s[2])
        pal_carro = [producto, cantidad]
        carro.append(pal_carro)

def checkout():
    global carro
    global catalogo
    precio = 0

    a = 0
    b = 0
    for producto in carro:
        precio += catalogo[(producto[0]-1)][2] * producto[1]
    for producto in carro:
        if producto[0] == 1 or producto[0] == 2 or producto[0] == 3:
            a += 1
        elif producto[0] == 4 or producto[0] == 5:
            b += 1
    # dctos
    if a == 3:
        precio = 0.8 * precio
    if b == 2:
        precio = 0.85 * precio
    return round(precio,1)

n = ''
while n != 'checkout':
    n = input('producto, cantidad: ')
    if n == 'ver':
        for producto in catalogo:
            print(producto)

    elif n == 'checkout':
        print(checkout())

    else:
        agregarcarro(n)