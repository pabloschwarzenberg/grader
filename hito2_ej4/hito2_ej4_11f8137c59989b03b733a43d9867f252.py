p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carrito = []
comprar = 1
cont1 = 0
cont2 = 0
cont3 = 0
cont4= 0
descuento1 = 0
descuento2 = 0
precios_= 0
while comprar ==1:
    op = int(input("Que desea hacer?\n1.- Agregar producto\n2.-Ver\n3.-Checkout\n4.-Salir"))
    if op == 1:
        comp = input("ingrese el producto y la cantidad que desea comprar")
        lista = comp.split(",")
        #print(lista)
        prod = int(lista[0])
        if prod == 1:
            n = int(lista[1])
            #print(n)
            for i in range(n):
                carrito.append(p1)
            #print(carrito)
        elif prod == 2:
            n = int(lista[1])
            #print(n)
            for i in range(n):
                carrito.append(p2)
            #print(carrito)
        elif prod == 3:
            n = int(lista[1])
            #print(n)
            for i in range(n):
                carrito.append(p3)
            #print(carrito)
        elif prod == 4:
            n = int(lista[1])
            #print(n)
            for i in range(n):
                carrito.append(p4)
            #print(carrito)
                    
    elif op==2:
        print(carrito)
        
    elif op ==3:
        #si esta p1,p2 y p3 se hace un descuento de 20%
        #Si esta 4 y 5 se hace un descuento del 15.
        for i in range(len(carrito)-1):
            esta_ = carrito[i][0]
            if esta_ == 1:
                cont1 += 1
            elif esta_ == 2:
                cont2 += 1
            elif esta_ == 3:
                cont3 += 1
            elif esta_ == 4:
                cont4 += 1
        if cont1!=0 and cont2!=0 and cont3!=0:
            descuento1 = 1
        if cont4!= 0 and cont5!=0:
            decuento2 = 1
        ###ahora vemos los precios.
        for i in range(len(carrito)):
            precios_ = carrito[i][2]
            precios_ += precios_
        if descuento1==1:
            precios_ = precios_ - precios_*0.2
            print("El precio que debe pagar es de: ",precios_)
            comprar = 2
        elif descuento2 == 1:
            precios_ = precios_ - precios_*0.15
            print("El precio que debe pagar es de: ",precios_)
            comprar = 2
        else:
            print("El precio que debe pagar es de: ",precios_)
            comprar = 4
    else:
        comprar = 4