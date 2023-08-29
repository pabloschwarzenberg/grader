p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

P=[p1[1:],p2[1:],p3[1:],p4[1:],p5[1:]]

precio1=(p1[2])
precio2=(p2[2])
precio3=(p3[2])
precio4=(p4[2])
precio5=(p5[2])
preciototal=0

cantidadp1=0
cantidadp2=0
cantidadp3=0
cantidadp4=0
cantidadp5=0

accion=0
carro=[]

def ver(carro):
    return carro

def agregar_producto(producto,cantidad):
    m=0
    if producto==1:
        while cantidad>m:
            carro.append(p1)
            m=m+1           
    if producto==2:
        while cantidad>m:
            carro.append(p2)
            m=m+1
    if producto==3:
        while cantidad>i:
            carro.append(p3)
            m=m+1
    if producto==4:
        while cantidad>m:
            carro.append(p4)
            m=m+1
    if producto==5:
        while cantidad>m:
            carro.append(p5)
            m=m+1

def checkout(cantidadp1,cantidadp2,cantidadp3,cantidadp4,cantidadp5):
    precio1=(p1[2])
    precio2=(p2[2])
    precio3=(p3[2])
    precio4=(p4[2])
    precio5=(p5[2])
    preciototal=0


    if cantidadp1>0 and cantidadp2>0 and cantidadp3>0 and cantidadp4>=0 and cantidadp5>=0:
        preciototal=preciototal+(precio4*cantidadp4+precio5*cantidadp5+precio3*cantidadp3+precio2*cantidadp2+precio1*cantidadp1)*80/100
        preciototal=round(preciototal,1)
        
    if  cantidadp4>0 and cantidadp5>0 and cantidadp3>=0 and cantidadp2>=0 and cantidadp1>=0:
        preciototal=preciototal+(precio4*cantidadp4+precio5*cantidadp5+precio3*cantidadp3+precio2*cantidadp2+precio1*cantidadp1)*85/100
        preciototal=round(preciototal,1)
    
    else:
        preciototal=preciototal+(precio4*cantidadp4+precio5*cantidadp5+precio3*cantidadp3+precio2*cantidadp2+precio1*cantidadp1)
        preciototal=round(preciototal,1)
    
    return preciototal

seguir=1
while seguir==1:
    accion=input("Que desea hacer?")
    accion=accion.lower()
    if accion=="ver":
        print(ver(carro))
        
    if "," in accion:
        producto=accion[0]
        producto=int(producto)
        cantidad=accion[2]
        cantidad=int(cantidad)
        agregar_producto(producto,cantidad)
        
    if accion=="checkout":
        cantidadp1=carro.count([1,"Pokemon X",33.77])
        cantidadp2=carro.count([2,"Nintendo XL",203])
        cantidadp3=carro.count([3,"Mario Kart 7",27.58])
        cantidadp4=carro.count([4,"PlayStation 4",348.00])
        cantidadp5=carro.count([5,"FIFA 16",51.19])
        
        seguir=2
        print(checkout(cantidadp1,cantidadp2,cantidadp3,cantidadp4,cantidadp5))
        