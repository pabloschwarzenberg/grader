p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
catalogo=[p1,p2,p3,p4,p5]
print(catalogo)
carro=[]
i=0

for producto in catalogo:
    print(i,producto)
    i=i+1
while i>0:
    item=input("Ingrese producto, cantidad: ")
    item=item.split(",")
    compra=[]
    j=0
    while j<len(carro):
            if carro[i][0]==compra[0]:
                carro[i][1]=compra[1]
                break
            i=i+1
    if i==len(carro):
            carro.append(compra)
    salir=input("Ver compra")
    
