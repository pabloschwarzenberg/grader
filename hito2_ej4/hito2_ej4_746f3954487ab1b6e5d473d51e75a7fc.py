p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

# Dictionary to store cart
cart = {}

# Asking user choice for actions again and again
while True:
    while True:  # For validation that user enters only 1, 2 or 3
        print(''' Escribe VER para ver el producto
   Escribe CART para mostrar el carrito
   Escribe CHECKOUT para pagar''')
        print()
        choice = input('Ingresar decisión: ')
        if choice in ('ver', 'cart', 'checkout'):
            print()
            break
        else:
            print('Favor ingresar la decisión correcta')
            print()

    if choice == 'ver':  # If choice is 1 then add products to cart
        print('''Ingrese el Número de producto y la cantidad de producto como número_producto.cantidad
    1: Pokemon X Game para Nintendo 3DS
    2: Nintendo 3DS XL
    3: Mario Kart 7 Game para Nintendo 3DS
    4: PlayStation 4
    5: FIFA 16, PlayStation 4''')

        while True:  # Validation to check if user asks correct input like 5.2
            product = input('Ingrese el número y la cantidad del producto como número_producto.cantidad (ejemplo 5,2):')
            check_list = product.split('.')
            if ((len(check_list) == 2) and (check_list[0] in ['1', '2', '3', '4', '5'])):

                if check_list[0] not in cart:  # If entered format is correct then add to cart
                    cart[check_list[0]] = int(check_list[1])
                else:
                    cart[check_list[0]] += int(check_list[1])
                print()
                break
            else:
                print('Ingresar la decisión en el formato correcto')
                print()


    elif choice == 'cart':  # If choice is 2, then print cart items
        print('Items actuales en el carrito:')
        for item in cart:
            if item == '1':
                precio = cart[item] * p1[2]
                print('Cantidad:', cart[item], '-- Item:', p1[1], '-- Precio: $', round(precio, 1))
            elif item == '2':
                precio = cart[item] * p2[2]
                print('Cantidad:', cart[item], '-- Item:', p2[1], '-- Precio: $', round(precio, 1))
            elif item == '3':
                precio = cart[item] * p3[2]
                print('Cantidad:', cart[item], '-- Item:', p3[1], '-- Precio: $', round(precio, 1))
            elif item == '4':
                precio = cart[item] * p4[2]
                print('Cantidad:', cart[item], '-- Item:', p4[1], '-- Precio: $', round(precio, 1))
            elif item == '5':
                precio = cart[item] * p5[2]
                print('Cantidad:', cart[item], '-- Item:', p5[1], '-- Precio: $', round(precio, 1))
        print()


    elif choice == 'checkout':  # If choice is 3, then print checkout price along with discount and total and end the program
        total = 0
        print('Precios a pagar')
        for item in cart:
            if item == '1':
                precio = cart[item] * p1[2]
                precio = precio - (0.2 * precio)
                print('Cantidad:', cart[item], '-- Item:', p1[1], '-- Precio: $', round(precio, 1))
            elif item == '2':
                precio = cart[item] * p2[2]
                precio = precio - (0.2 * precio)
                print('Cantidad:', cart[item], '-- Item:', p2[1], '-- Precio: $', round(precio, 1))
            elif item == '3':
                precio = cart[item] * p3[2]
                precio = precio - (0.2 * precio)
                print('Cantidad:', cart[item], '-- Item:', p3[1], '-- Precio: $', round(precio, 1))
            elif item == '4':
                precio = cart[item] * p4[2]
                precio = precio - (0.15 * precio)
                print('Cantidad:', cart[item], '-- Item:', p4[1], '-- Precio: $', round(precio, 1))
            elif item == '5':
                precio = cart[item] * p5[2]
                precio = precio - (0.15 * precio)
                print('Cantidad:', cart[item], '-- Item:', p5[1], '-- Precio: $', round(precio, 1))

            total += precio
        print('Precio total: $', round(total, 1))
        break