productos =[[1,"Pokemon X",33.77],[2,"Nintendo XL",203],[3,"Mario Kart 7",27.58],
            [4,"PlayStation 4",348.00], [5,"FIFA 16",51.19]]

def producto_cantidad(pc,carro,producs):
    pu = pc.split(",")
    producto = int(pu[0])
    cantidad = int(pu[1])
    lis = []
    for i in range(len(producs)):
        if producs[i][0] == producto:
            if carro == []:
                lis.append(producs[i][0])
                lis.append(producs[i][1])
                lis.append((producs[i][2])*cantidad)
                carro.append(lis)
            else:
                con = 0
                ti = 0
                for k in range(len(carro)):
                        if carro[k][0] == producto:
                            con += 1
                            ti = k
                if con > 0:
                    carro[ti][2] += (carro[ti][2])*cantidad
                else:
                    lis.append(producs[(producto-1)][0])
                    lis.append(producs[(producto-1)][1])
                    lis.append((producs[(producto-1)][2])*cantidad)
                    carro.append(lis)
            
    return carro

def imprimir(carro):
    for i in range(len(carro)):
        print(carro[i])

def check(carro):
    desc1 = [1,2,3]
    desc2 = [4,5]
    ld1 = []
    ld2 = []
    total = 0
    for t in range(len(carro)):
        total += carro[t][2]
    for a in range(len(carro)):
        if carro[a][0] == 1 or 2 or 3:
            ld1.append(carro[a][0])
        if carro[a][0] == 4 or 5:
            ld2.append(carro[a][0])
    ki = 0
    for b in range(len(desc1)):
        if desc1[b] in ld1:
            ki+=1
    ko = 0
    for c in range(len(desc2)):
        if desc2[c] in ld2:
            ko+=1
    if ki >= 3:
        desc = (total*20)/100
        totalF = total-desc
        totalF = round(totalF,1)
        return totalF
    if ko >= 2:
        desc = (total*15)/100
        totalF = total-desc
        totalF = round(totalF,1)
        return totalF
    else:
        totalF = total
        totalF = round(totalF,1)
        return totalF
    
            
seguir = True
carrito = []
while seguir:
    accion = input("Tu sabes:")
    if "," in accion:
        carrito = producto_cantidad(accion,carrito,productos)
    if accion == "ver":
        a = imprimir(carrito)
    if accion == "checkout":
        salida = check(carrito)
        print(salida)
        seguir = False