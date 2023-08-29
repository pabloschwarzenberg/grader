prod_cant=input("Que hacer: ")
productos=[]
totales=[]
while prod_cant!="checkout":
    
    if prod_cant=="ver":
        for i in productos:
            print(i)
    else:
        productos.append(prod_cant)
        cantidad=int(prod_cant[2])
        if prod_cant[0]=="1":
            descuento=0.2
            precio=33.77
        elif prod_cant[0]=="2":
            descuento=0.2
            precio=203
        elif prod_cant[0]=="3":
            descuento=0.2
            precio=27.58
        elif prod_cant[0]=="4":
            descuento=0.15
            precio=348
        elif prod_cant[0]=="5":
            descuento=0.15
            precio=51.19
        totales.append(round(precio*cantidad*(1-descuento),1))
    prod_cant=input("Que hacer: ")    
if prod_cant=="checkout":
    for i in totales:
        print(i)       