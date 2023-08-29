p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro=[]
def agregar_producto(producto,cantidad):
    if producto==1:
        carro.append(p1)
        carro.append(cantidad)
    elif producto==2:
        carro.append(p2)
        carro.append(cantidad)
    elif producto==3:
        carro.append(p3)
        carro.append(cantidad)
    elif producto==4:
        carro.append(p4)
        carro.append(cantidad)
    elif producto==5:
        carro.append(p5)
        carro.append(cantidad)
    else:
        print("Producto no existe")
def ver_carro():
    print("Carro de compras:")
    for i in range(0,len(carro),2):
        print(carro[i][1],"x",carro[i+1])
def checkout():
    total=0
    for i in range(0,len(carro),2):
        total= total + (carro[i][2]*carro[i+1])
    if len(carro)==2:
        total=total*0.8
    elif len(carro)==4:
        total=total*0.85
    print("Total a pagar:",round(total,1))
while True:
    orden=input("Ingrese orden: ")
    if orden=="ver":
        ver_carro()
    elif orden=="checkout":
        checkout()
        break
    else:
        orden=orden.split(",")
        agregar_producto(int(orden[0]),int(orden[1]))