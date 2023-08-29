p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
lista=[]
menu = p1,p2,p3,p4,p5
producto1=0
producto2=0
producto3=0
producto4=0
producto5=0
total=0
cantidades= ""
while cantidades != "checkout":
    if cantidades != "ver" and cantidades != "checkout":
        for opcion in menu:
            print(opcion)
    cantidades = input("Ingrese el producto , cantidad:  ")
    if cantidades != "checkout" and cantidades != "ver":
        lista.append(cantidades)
    if cantidades == "ver":
        for i in lista:
            producto = i[0]
            cantidad = i[2]
            print(menu[int(producto)-1], cantidad)
    if cantidades == "checkout":
        for i in lista:
            producto = i[0]
            cantidad = i[2]
            precio = menu[int(producto) - 1][2]

            total=total + (precio * int(cantidad))

            if producto == "1":
                producto1=1
            if producto == "2":
                producto2=1
            if producto == "3":
                 producto3=1
            if producto == "4":
                producto4=1
            if producto == "5":
                     producto5=1

        
        oferta1=producto1 + producto2 + producto3
        oferta2=producto4 + producto5
        if oferta1 == 3:
            total = total*0.8
        elif oferta2 == 2:
            total = total*0.85
        else:
            pass
        print(total)      