p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
productos=[p1,p2,p3,p4,p5]
carro=[]
while True:
    opcion=input()
    if opcion=="ver":
        print(carro)
    elif opcion=="checkout":
        costo=0
        for n in range(len(carro)):
            costo+=int(carro[n][2])
            print(costo)
    else:
        agregar=opcion.split(",")
        for n in range(int(agregar[1])):
            y=int(agregar[0])
            carro.append(productos[y-1])
    
    