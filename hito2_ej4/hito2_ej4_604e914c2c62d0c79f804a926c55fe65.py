p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
P=[p1[1:3],p2[1:3],p3[1:3],p4[1:3],p5[1:3]]
c1=(p1[2])
c2=(p2[2])
c3=(p3[2])
c4=(p4[2])
c5=(p5[2])
ct=0
cp1=0
cp2=0
cp3=0
cp4=0
cp5=0
Qd=0
carro=[]
def mostrar(carro):
    return carro
def agregar_producto(p,a):
    i=0
    if p==1:
        while a>i:
            carro.append(p1)
            i=i+1           
    if p==2:
        while a>i:
            carro.append(p2)
            i=i+1
    if p==3:
        while a>i:
            carro.append(p3)
            i=i+1
    if p==4:
        while a>i:
            carro.append(p4)
            i=i+1
    if p==5:
        while a>i:
            carro.append(p5)
            i=i+1

def checkout(cp1,cp2,cp3,cp4,cp5):
    c1=(p1[2])
    c2=(p2[2])
    c3=(p3[2])
    c4=(p4[2])
    c5=(p5[2])
    costo_total=0
    if  cp4>0 and cp5>0 and cp3>=0 and cp2>=0 and cp1>=0:
        costo_total=costo_total+(c4*cp4+c5*cp5+c3*cp3+c2*cp2+c1*cp1)*85/100
        costo_total=round(costo_total,1)
    if cp1>0 and cp2>0 and cp3>0 and cp4>=0 and cp5>=0:
        costo_total=costo_total+(c4*cp4+c5*cp5+c3*cp3+c2*cp2+c1*cp1)*80/100
        costo_total=round(costo_total,1)
    else:
        costo_total=costo_total+(c4*cp4+c5*cp5+c3*cp3+c2*cp2+c1*cp1)
        costo_total=round(costo_total,1)
    return costo_total
continuar=1
while continuar==1:
    Qd=input("Que desea hacer?")
    Qd=Qd.lower()
    if Qd=="ver":
        print(ver(carro))
    if "," in Qd:
        pro=Qd[0]
        pro=int(pro)
        can=Qd[2]
        can=int(can)
        agregar_producto(pro,can)
    if Qd=="checkout":
        cp1=carro.count([1,"Pokemon X",33.77])
        cp2=carro.count([2,"Nintendo XL",203])
        cp3=carro.count([3,"Mario Kart 7",27.58])
        cp4=carro.count([4,"PlayStation 4",348.00])
        cp5=carro.count([5,"FIFA 16",51.19])
        continuar=2
        print(checkout(cp1,cp2,cp3,cp4,cp5))