p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos=[p1,p2,p3,p4,p5]
carro=[]

def checkout(carro):
    descuento=0
    compras=[]
    valor=0
    for item in carro:
        compras.append(item[0])
        valor=valor+item[0][2]*item[1]
    if p1 in compras and p2 in compras and p3 in compras:
        descuento+=0.2
    if p4 in compras and p5 in compras:
        descuento+=0.15
    precio=valor-valor*descuento
    return precio

while True:
    orden=input("Ingrese operacion: ")
    orden=orden.strip().lower()
    if orden.find(",")!=-1:
        datos=orden.split(",")
        datos=list(map(int,datos))
        p=productos[datos[0]-1]
        carro.append([p,datos[1]])
    elif orden=="checkout":
        precio=checkout(carro)
        print("El valor a pagar es",round(precio,1))
        break
    elif orden=="ver":
        for item in carro:
            print(item[0][1],item[1])



