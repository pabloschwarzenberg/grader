p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productoss = p1, p2, p3, p4, p5
precio_de_productos = productoss[2]

c_p1 = 0
c_p2 = 0
c_p3 = 0
c_p4 = 0
c_p5 = 0

while True:
    inicio = input("¿Que productos y cuantos quieres comprar?: ")
    if inicio == "ver":
        if c_p1 > 0:
            print("{}...{}".format(c_p1, p1[1]))
        if c_p2 > 0:
            print("{}...{}".format(c_p2, p2[1]))
        if c_p3 > 0:
            print("{}...{}".format(c_p3, p3[1]))
        if c_p4 > 0:
            print("{}...{}".format(c_p4, p4[1]))
        if c_p5 > 0:
            print("{}...{}".format(c_p5, p5[1]))
    elif inicio == "checkout":

        total = c_p1*p1[2] + c_p2*p2[2] + c_p3*p3[2] + c_p4*p4[2] + c_p5 * p5[2]

        if c_p1 > 0 and c_p2 > 0 and c_p3 > 0:
            total = total * 0.8

        elif c_p4 > 0 and c_p5 > 0:
            total = total * 0.85

        print("El total es: {}".format(round(total,1)))
        break

    else:
        producto_cantidad = inicio.split(",")
        producto = int(producto_cantidad[0])
        cantidad = int(producto_cantidad[1])

        if producto == p1[0]:
            c_p1 += cantidad
        elif producto == p2[0]:
            c_p2 += cantidad
        elif producto == p3[0]:
            c_p3 += cantidad
        elif producto == p4[0]:
            c_p4 += cantidad
        elif producto == p5[0]:
            c_p5 += cantidad



