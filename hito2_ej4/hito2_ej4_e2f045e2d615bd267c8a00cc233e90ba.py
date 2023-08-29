carrito = []
p1 = [1, 'Pokemon X', 33.77]
p2 = [2, 'Nintendo XL', 203]
p3 = [3, 'Mario Kart 7', 27.58]
p4 = [4, 'PlayStation 4', 348.00]
p5 = [5, 'FIFA 16', 51.19]
productos_descuento_20 = [p1, p2, p3]
productos_descuento_15 = [p4, p5]
def ver():
    print('Carrito de compras:')
    for producto, cantidad in carrito:
        print('Producto:', producto[1])
        print('Cantidad:', cantidad)
        print('__________________________________________________________________')

def aplicar_descuentos():
    for producto, cantidad in carrito:
        if producto in productos_descuento_20:
            producto[2] *= 0.8
        elif producto in productos_descuento_15:
            producto[2] *= 0.85

def calcular_precio_total():
    total = 0
    for producto, cantidad in carrito:
        total += producto[2] * cantidad
    return total

def checkout():
    print('____________________________________________________________________________________________________________________________________')
    print('Detalles de la compra:')
    for producto, cantidad in carrito:
        precio_con_descuento = producto[2]
        if producto in productos_descuento_20:
            precio_con_descuento *= 0.8
        elif producto in productos_descuento_15:
            precio_con_descuento *= 0.85 
        
        print('Producto:', producto[1])
        print('Cantidad:', cantidad)
        print('Precio unitario:', producto[2])
        print('Precio con descuento:', precio_con_descuento)
        print('____________________________________________________________________________________________________________________________________')

    total = calcular_precio_total()
    print('Su precio total es:', round(total, 1))

###########MAIN############
while True:
    entrada = input('Ingrese el producto y la cantidad en el formato ''producto,cantidad'' (o ''ver'' para mostrar el carrito, ''checkout'' para realizar el pago): ')
    
    if entrada.lower() == 'ver':
        ver()
    elif entrada.lower() == 'checkout':
        checkout()
        break
    else:
        try:
            p_in, cantidad = entrada.split(',')
            p_in =int(p_in)
            cantidad = int(cantidad)

            if p_in == 1:
                producto = p1
            elif p_in == 2:
                producto = p2
            elif p_in == 3:
                producto = p3
            elif p_in == 4:
                producto = p4
            elif p_in == 5:
                producto = p5
                continue
            else:
                print('Producto no encontrado')
                continue
            carrito.append((producto, cantidad))

        except ValueError:
             print('Error, intentelo denuevo.')
             print('____________________________________________________________________________________________________________________________________')

      