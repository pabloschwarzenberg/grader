p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

lista_de_compras = []
while True:
    compra = str(input())
    lista_de_compras.append(compra)
    if compra == "checkout":
        cantidad_p1 = []
        cantidad_p2 = []
        cantidad_p3 = []
        cantidad_p4 = []
        cantidad_p5 = []
        precio_1 = 33.77
        precio_2 = 203
        precio_3 = 27.58
        precio_4 = 348.00
        precio_5 = 51.19
        for elemento in lista_de_compras:
            if elemento[0] == "1":
                i = 0
                while i < int(elemento[2]):
                    cantidad_p1.append(elemento[0])
                    i += 1
            elif elemento[0] == "2":
                i = 0
                while i < int(elemento[2]):
                    cantidad_p2.append(elemento[0])
                    i += 1
            elif elemento[0] == "3":
                i = 0
                while i < int(elemento[2]):
                    cantidad_p3.append(elemento[0])
                    i += 1
            elif elemento[0] == "4":
                i = 0
                while i < int(elemento[2]):
                    cantidad_p4.append(elemento[0])
                    i += 1
            elif elemento[0] == "5":
                i = 0
                while i < int(elemento[2]):
                    cantidad_p5.append(elemento[0])
                    i += 1
            else:
                break
        repeticiones_1 = int(cantidad_p1.count("1"))
        repeticiones_2 = int(cantidad_p2.count("2"))
        repeticiones_3 = int(cantidad_p3.count("3"))
        repeticiones_4 = int(cantidad_p4.count("4"))
        repeticiones_5 = int(cantidad_p5.count("5"))

        valor_total = repeticiones_1*precio_1 + repeticiones_2*precio_2 + repeticiones_3*precio_3 + repeticiones_4*precio_4 + repeticiones_5*precio_5

        if repeticiones_1 > 0 and repeticiones_2 > 0 and repeticiones_3 > 0:
            if repeticiones_4 > 0 and repeticiones_5 > 0:
                valor_total_con_descuento = valor_total * 0.75
                print(round(valor_total_con_descuento,1))
            elif (repeticiones_4 == 0 and repeticiones_5 > 0) or (repeticiones_4 > 0 and repeticiones_5 == 0):
                valor_total_con_descuento = valor_total*0.8
                print(round(valor_total_con_descuento,1))
            elif repeticiones_4 == 0 and repeticiones_5 == 0:
                valor_total_con_descuento = valor_total * 0.8
                print(round(valor_total_con_descuento,1))
        elif repeticiones_4 > 0 and repeticiones_5 > 0:
            if repeticiones_1 > 0 and repeticiones_2 != 0 and repeticiones_3 > 0:
                valor_total_con_descuento = valor_total * 0.75
                print(round(valor_total_con_descuento,1))
            else:
                valor_total_con_descuento = valor_total * 0.85
                print(round(valor_total_con_descuento,1))
        else:
            print(round(valor_total,1))