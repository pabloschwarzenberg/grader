p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

lista_productos = [p1, p2, p3, p4, p5]
producto = []
carro = input()
while carro != "checkout" and carro != "ver":
    

    producto.append(carro)


    lista_cantidades = []
    lista_producto = []

    for i in range(0,len(producto)):
        producto_cambiado = producto[i]
        if producto_cambiado != "checkout" and producto_cambiado != "ver" and producto_cambiado != "no":
            producto_cambiado = int(producto_cambiado[0])
            lista_producto.append(producto_cambiado)

        cantidad = producto[i]
        if cantidad != "checkout" and cantidad != "ver" and producto_cambiado != "no":
            cantidad = int(cantidad[2])
            lista_cantidades.append(cantidad)

    lista_valores = []

    for i in range(0,len(lista_producto)):
        if 1 == lista_producto[i]:
            lista_valores.append(33.77)
        elif 2 == lista_producto[i]:
            lista_valores.append(203)
        elif 3 == lista_producto[i]:
            lista_valores.append(27.58)
        elif 4 == lista_producto[i]:
            lista_valores.append(348.00)
        elif 5 == lista_producto[i]:
            lista_valores.append(51.19)

            
    valor_total = 0
    for i in range(0,len(lista_valores)):
        valor_total = lista_valores[i] * lista_cantidades[i] + valor_total
    if 1 in lista_producto and 2 in lista_producto and 3 in lista_producto:
        descuento = (valor_total * 20)/100
        valor_total = valor_total - descuento
    if 4 in lista_producto and 5 in lista_producto:
        descuento = (valor_total * 15)/100
        valor_total = valor_total - descuento
    valor_redondeado= round(valor_total,1)

    carro = input("quiere algo mas = ")
        
if carro == "ver":
    print("1: Juego Pokemon X para Nintendo 3DS, USD 33.77 \n 2: Nintendo 3DS XL, USD 203 \n 3: Juego Mario Kart 7 para Nintendo 3DS, USD 27.58 \n 4: PlayStation 4, USD 348.00 \n 5: FIFA 16, PlayStation 4, USD 51.19")

if carro == "checkout":
    print(valor_redondeado)


