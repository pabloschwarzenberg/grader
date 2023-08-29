p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro = [0,0,0,0,0]
precio = 0
prdct = [p1,p2,p3,p4,p5]
while True:
    a = input()
    if a == "ver":
        pass
    if a == "checkout":
        for i in range(5):
            precio += carro[i] * prdct[i][2]
        if carro[0] != 0 and carro[1] != 0 and carro[2] != 0:
            precio = (precio * 80)/100
        if carro[3] != 0 and carro[4] != 0:
            precio = (precio * 85)/100
        precio = round(precio,1)
        print(precio)
        break  
    else:
        p = int(a[0])
        c = int(a[2])
        carro[p - 1] = carro[p - 1] + c
        