p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
catalogo=[p1,p2,p3,p4,p5]
carro=[]

terminar=False
i=0
for producto in catalogo:
    print(i,producto)
    i=i+1
while not terminar:
    #item=input("ingrese producto, cantidad")
    #item=item.split(",")
    compra=[float(item[0]),float(item[1])]
    #carro.append(compra)
    i=0
    while i< len(carro):
        if carro[i][0]==compra[0]:
            carro[i][1]=compra[1]
            break
        i=i+1
    if i==len(carro):
        carro.append(compra)
    salir=input("desea salir?")
    if salir.lower()=="s":
        terminar=True  