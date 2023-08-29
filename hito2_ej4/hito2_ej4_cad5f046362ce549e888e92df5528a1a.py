p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

def agregar_carrito(ped,st):
    if ped[0]=="1":
        p1[3] = True
        p1[4] = int(ped[1])
        p1[5] = p1[4]*p1[2]
        st = st + p1[5]
    elif ped[0]=="2":
        p2[3] = True
        p2[4] = int(ped[1])
        p2[5] = p2[4]*p2[2]
        st = st + p2[5]
    elif ped[0]=="3":
        p3[3] = True
        p3[4] = int(ped[1])
        p3[5] = p3[4]*p3[2]
        st = st + p3[5]
    elif ped[0]=="4":
        p4[3] = True
        p4[4] = int(ped[1])
        p4[5] = p4[4]*p4[2]
        st = st + p4[5]
    elif ped[0]=="5":
        p5[3] = True
        p5[4] = int(ped[1])
        p5[5] = p5[4]*p5[2]
        st = st + p5[5]
    return st

def verificar_compra(st):
    t = 0
    desc123 = 0
    if p1[3] and p2[3] and p3[3]:
        desc123 = st * 0.2
    desc45 = 0
    if p4[3] and p5[3]:
        desc45 = st * 0.15
    t = st - (desc123 + desc45)
    return t
      