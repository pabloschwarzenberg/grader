

def checkout(lista_productos:list, carrito:dict):

    descuento = 0
    subtotal = 0

    productos = carrito.keys()
    
    if 1 in productos and 2 in productos and 3 in productos:
        descuento = descuento + 0.3
    
    if 4 in productos and 5 in productos:
        descuento = descuento + 0.15

    for item in lista_productos:
        if item[0] in productos:
            precio = float(item[2])
            subtotal_producto = carrito[item[0]] * precio

            subtotal = subtotal + subtotal_producto
            print(item[1] + ' $' + str(float(round(subtotal_producto, 1))))    

    total = subtotal - (subtotal * descuento)

    return round(total, 1)

p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos = [p1, p2, p3, p5, p5]

carrito = {}
subtotal = 0

while True:

    opcion = input("Ingrese su opcion (ver / checkout / producto): ")

    if opcion.lower() == 'ver':
        for item in productos:
            print(item)
        
    elif opcion.lower() == 'checkout':
        break

    # opcion de compra
    else:
        prod = int(opcion.split(',')[0])
        cantidad = int(opcion.split(',')[1])

        carrito[prod] = cantidad


print('TOTAL: $' + str(checkout(productos, carrito)))