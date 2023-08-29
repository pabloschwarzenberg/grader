p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

total = 0
t_desc = 0

def cajero (lista_compras):
    
    total = 0
    t_desc = []
    for i in range(len(lista_compras)):
        p = lista_compras[i][0]
        c = lista_compras[i][2]
        Cond = (int(p)>=1) and (int(p)<=5)
        while(Cond):
            p = int(p)
            c = int(c)
            if(p == 1):
                p_p = p1[2] *c
                total = total+p_p
                t_desc += "1"
                break
            elif(p == 2):
                p_p = p2[2] *c
                total = total+p_p           
                t_desc += "2"
                break
            elif(p == 3):
                p_p = p3[2] *c 
                total = total+p_p
                t_desc += "3"
                break
            elif(p == 4):
                p_p = p4[2] *c
                total = total+p_p
                t_desc += "4"
                break
            elif(p == 5):
                p_p = p5[2] *c
                total = total+p_p
                t_desc += "5"
                break

    if(1 in t_desc)and(2 in t_desc)and(3 in t_desc):
        desc = total/5
        total = total-desc
    elif(4 in t_desc)and(5 in t_desc):
        desc = (total*15)/100
        total = total-desc

    total = round(total,1)

    return total

carrito = []

while(True):
    product = input("Ingrese su compra: ")

    if(product == "checkout"):
        print(cajero(carrito))
        break
    elif(product == "ver"):
        print(carrito)
        pass
    else:
        product = list(product)
        carrito.append(product)