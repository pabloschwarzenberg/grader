p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

def separar(compra):
    funcion=compra[-1]
    productos=compra[:-1]
    return productos, funcion
def checkout(productos,p1,p2,p3,p4,p5):
    Vt=0
    prod=[]
    #lista solo productos
    for i in productos:
        prod.append(i[0])
    #calor sin descuentos
    for i in productos:
        if i[0]=="1":
            Vt+=p1[2]*int(i[2])
        elif i[0]=="2":
            Vt+=p2[2]*int(i[2])
        elif i[0]=="3":
            Vt+=p3[2]*int(i[2])
        elif i[0]=="4":
            Vt+=p4[2]*int(i[2])
        elif i[0]=="5":
            Vt+=p5[2]*int(i[2])
    #descuentos
    if  (('1' in prod) and ('2' in prod) and ('3' in prod)
         and ('4' in prod) and ('5' in prod)):
        Vt-=Vt*0.35
    elif  ('1' in prod) and ('2' in prod) and ('3' in prod):
        Vt-=Vt*0.20
    elif  ('4' in prod) and ('5' in prod):
        Vt-=Vt*0.15
    Vt=round(Vt,1)
    print(Vt)

def ver(productos,p1,p2,p3,p4,p5):
    for i in productos:
        if i[0]=="1":
            for e in range(0,int(i[2])):
                print(p1[1])
        if i[0]=="2":
            for e in range(0,int(i[2])):
                print(p2[1])
        if i[0]=="3":
            for e in range(0,int(i[2])):
                print(p3[1])
        if i[0]=="4":
            for e in range(0,int(i[2])):
                print(p4[1])
        if i[0]=="5":
            for e in range(0,int(i[2])):
                print(p5[1])
                        
#ENTRADAS
compra=[]
comprar=""
while comprar!="checkout" and comprar!="ver":
    comprar=input("ingrese producto a comprar: ")
    compra.append(comprar)
separado=separar(compra)
productos=separado[0]
funcion=separado[1]
#SALIDAS
if funcion=="checkout":
    checkout(productos,p1,p2,p3,p4,p5)
elif funcion=="ver":
    ver(productos,p1,p2,p3,p4,p5)
