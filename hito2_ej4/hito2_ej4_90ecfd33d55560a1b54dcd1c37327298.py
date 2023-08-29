p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos2 = p1, p2, p3, p4, p5
precio = productos2[2]

cantidad1 = 0
cantidad2 = 0
cantidad3 = 0
cantidad4 = 0
cantidad5 = 0

while True:
    instruccion = input("Indique el producto y la cantidad que comprará: ")
    if instruccion == "ver":
        if cantidad1 > 0:
            print("{}...............{}".format(cantidad1, p1[1]))
        if cantidad2 > 0:
            print("{}...............{}".format(cantidad2, p2[1]))
        if cantidad3 > 0:
            print("{}...............{}".format(cantidad3, p3[1]))
        if cantidad4 > 0:
            print("{}...............{}".format(cantidad4, p4[1]))
        if cantidad5 > 0:
            print("{}...............{}".format(cantidad5, p5[1]))
    elif instruccion == "checkout":

        total = cantidad1*p1[2] + cantidad2*p2[2] + cantidad3*p3[2] + cantidad4*p4[2] + cantidad5*p5[2]

        if cantidad1 > 0 and cantidad2 > 0 and cantidad3 > 0:
            total = total * 0.8

        elif cantidad4 > 0 and cantidad5 > 0:
            total = total * 0.85

        print("El total es: {}".format(round(total,1)))
        break

    else:
        producto_cantidad = instruccion.split(",")
        producto = int(producto_cantidad[0])
        cantidad = int(producto_cantidad[1])

        if producto == p1[0]:
            cantidad1 += cantidad
        elif producto == p2[0]:
            cantidad2 += cantidad
        elif producto == p3[0]:
            cantidad3 += cantidad
        elif producto == p4[0]:
            cantidad4 += cantidad
        elif producto == p5[0]:
            cantidad5 += cantidad
