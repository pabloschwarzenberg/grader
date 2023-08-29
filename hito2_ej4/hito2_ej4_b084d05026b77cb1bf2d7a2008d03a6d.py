p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos = [p1, p2, p3, p4, p5]
carro = []
carro1= []
monto = 0

def agregar_carro(producto_cantidad):
    carro1.append(producto_cantidad)
    c = []
    for i in producto_cantidad:
        if i in "0123456789":
            c.append(int(i))
    carro.append(c)

def calcular_precio(carro):
    M = []
    descuento_20 = False
    decuento_15 = False
    for item in carro:
        M.append(item[0])
        monto = monto + (item[1])*productos[(item[0] - 1)][2]
    if 1 and 2 and 3 in M:
        descuento_20 = True
    if 4 and 5 in M:
        descuento_15 = True
    if descuento_20:
        d1 = (p1[2] + p2[2] + p3[2])*0.20
        monto = monto - d1
    if descuento_15:
        d2 = (p4[2] + p5[2])*0.15
        monto = monto - d2
    monto = round(monto, 1)

orden = input()
for i in orden:
    if i == "ver":
        print(carro1)
        break
    elif i == "checkout":
        calcular_precio(carro)
        print (monto)
        break
    agregar_carro(i)