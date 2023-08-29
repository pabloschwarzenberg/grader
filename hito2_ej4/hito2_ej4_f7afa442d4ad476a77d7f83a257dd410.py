p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos_2 = p1, p2, p3, p4, p5
precio_precio = productos_2[2]

cantidad_p1 = 0
cantidad_p2 = 0
cantidad_p3 = 0
cantidad_p4 = 0
cantidad_p5 = 0

while True:
    instruccion = input("Producto y cantidad que deseas comprar: ")
    if instruccion == "ver":
        if cantidad_p1 > 0:
            print("{}...............{}".format(cantidad_p1, p1[1]))
        if cantidad_p2 > 0:
            print("{}...............{}".format(cantidad_p2, p2[1]))
        if cantidad_p3 > 0:
            print("{}...............{}".format(cantidad_p3, p3[1]))
        if cantidad_p4 > 0:
            print("{}...............{}".format(cantidad_p4, p4[1]))
        if cantidad_p5 > 0:
            print("{}...............{}".format(cantidad_p5, p5[1]))
    elif instruccion == "checkout":
        ###
        #cant_packs = min(cantidad_p1, cantidad_p2, cantidad_p3)
        #cost_un_pack = p1[2] + p2[2] + p3[2]
        #descuento = cost_un_pack * cant_packs * 0.8

        #cant_packs2 = min(cantidad_p4, cantidad_p5)
        #cost_un_pack2 = p4[2] + p5[2]
        #descuento_2 = cost_un_pack2 * cant_packs2 * 0.85

        total = cantidad_p1*p1[2] + cantidad_p2*p2[2] + cantidad_p3*p3[2] + cantidad_p4*p4[2] + cantidad_p5*p5[2]

        if cantidad_p1 > 0 and cantidad_p2 > 0 and cantidad_p3 > 0:
            total = total * 0.8

        elif cantidad_p4 > 0 and cantidad_p5 > 0:
            total = total * 0.85

        print("El total es: {}".format(round(total,1)))
        break

    else:
        producto_cantidad = instruccion.split(",")
        producto = int(producto_cantidad[0])
        cantidad = int(producto_cantidad[1])

        if producto == p1[0]:
            cantidad_p1 += cantidad
        elif producto == p2[0]:
            cantidad_p2 += cantidad
        elif producto == p3[0]:
            cantidad_p3 += cantidad
        elif producto == p4[0]:
            cantidad_p4 += cantidad
        elif producto == p5[0]:
            cantidad_p5 += cantidad