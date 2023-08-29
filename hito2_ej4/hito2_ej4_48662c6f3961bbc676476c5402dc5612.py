p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos = [[1,33.77],[2,203],[3,27.58],[4,348.00],[5,51.19]]

orden = ""
carro = []
precios = []
while orden != "checkout":
     
    orden = input()

    if orden == "ver":
        print(p1)
        print(p2)
        print(p3)
        print(p4)
        print(p5)
    
    elif orden == "checkout":
        total = sum(precios)
        if p1[0] in carro and p2[0] in carro and p3[0] in carro:
            total -= 0.2*total

        if p4[0] and p5[0] in carro:
            total -= 0.15*total

        print(round(total, 1))

    else:
        producto = int(orden.split(',')[0])
        cantidad = int(orden.split(',')[1])

        for i in range(len(productos)):
            if productos[i][0] == producto:
                carro.append(producto)
                precios.append(productos[i][1] * cantidad)     