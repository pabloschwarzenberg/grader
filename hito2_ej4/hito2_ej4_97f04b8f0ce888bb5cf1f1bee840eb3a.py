p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

Carrito = []

while True:
    opcion = input()
    if opcion == "ver":
        print(Carrito)
    if opcion == "checkout":
        Total = 0
        Tipos = []
        for Elemento in Carrito:
            if Elemento[0] == "1":
                Total = Total + p1[2]*int(Elemento[1])
                if Elemento[0] not in Tipos:
                    Tipos.append(Elemento[0])
            if Elemento[0] == "2":
                Total = Total + p2[2]*int(Elemento[1])
                if Elemento[0] not in Tipos:
                    Tipos.append(Elemento[0])
            if Elemento[0] == "3":
                Total = Total + p3[2]*int(Elemento[1])
                if Elemento[0] not in Tipos:
                    Tipos.append(Elemento[0])
            if Elemento[0] == "4":
                Total = Total + p4[2]*int(Elemento[1])
                if Elemento[0] not in Tipos:
                    Tipos.append(Elemento[0])
            if Elemento[0] == "5":
                Total = Total + p5[2]*int(Elemento[1])
                if Elemento[0] not in Tipos:
                    Tipos.append(Elemento[0])
        
        if "1" in Tipos and "2" in Tipos and "3" in Tipos:
            Total = Total * 0.8
            print(Total)
            break
        elif "4" in Tipos and "5" in Tipos:
            Total = Total * 0.85
            print(Total)
            break
        else:
            print(Total)
            break
    else:
        Compra = opcion.split(",")
        Carrito.append(Compra)