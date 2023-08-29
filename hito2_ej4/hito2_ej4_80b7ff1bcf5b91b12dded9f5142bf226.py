def agregar_producto(carro,producto,cantidad):
    p1=[1,"Pokemon X",33.77]
    p2=[2,"Nintendo XL",203]
    p3=[3,"Mario Kart 7",27.58]
    p4=[4,"PlayStation 4",348.00]
    p5=[5,"FIFA 16",51.19]
    if producto==1:
        carro.append([p1[0],p1[1],cantidad*p1[2]])
    elif producto==2:
        carro.append([p2[0],p2[1],cantidad*p2[2]])
    elif producto==3:
        carro.append([p3[0],p3[1],cantidad*p3[2]])
    elif producto==4:
        carro.append([p4[0],p4[1],cantidad*p4[2]])
    elif producto==5:
        carro.append([p5[0],p5[1],cantidad*p5[2]])
    return carro
    
carro=[]
total=0
accion=input("¿Que desea hacer?\Para agregar producto ingrese 'producto,cantidad'\nPara ver su carro ingrese 'ver'\nPara hacer checkout ingrese'checkout'")
accion=accion.lower()
while accion!="checkout":
    if accion=="ver":
        print(carro)
    else:
        producto=int(accion[0])
        cantidad=int(accion[2])
        carro=agregar_producto(carro,producto,cantidad)
    accion=input("¿Que desea hacer?\Para agregar producto ingrese 'producto,cantidad'\nPara ver su carro ingrese 'ver'\nPara hacer checkout ingrese'checkout'")
    accion=accion.lower()

carro.sort()
descuento1=0
descuento2=0
total=0

if ("Pokemon X" in carro[0]) and ("Nintendo XL" in carro[1]) and ("Mario Kart 7" in carro[2]):
    for i in range(0,3):
        descuento1=descuento1+carro[i][2]
    descuento1=descuento1*0.2

if len(carro)==2:
    if ("PlayStation 4" in carro[0]) and ("FIFA 16" in carro[1]):
        for i in range(len(carro)):
            decuento2=descuento2+carro[i][2]
        descuento2=descuento2*0.15

elif len(carro)==3:
    if ("PlayStation 4" in carro[1]) and ("FIFA 16" in carro[2]):
        for i in range(1,len(carro)):
            descuento2=descuento2+carro[i][2]
        descuento2=descuento2*0.15
elif len(carro)==4:
    if ("PlayStation 4" in carro[2]) and ("FIFA 16" in carro[3]):
        for i in range(2,len(carro)):
            descuento2=descuento2+carro[i][2]
        descuento2=descuento2*0.15
elif len(carro)==5:
    if ("PlayStation 4" in carro[3]) and ("FIFA 16" in carro[4]):
        for i in range(3,len(carro)):
            descuento2=descuento2+carro[i][2]
        descuento2=descuento2*0.15

for i in range(len(carro)):
    total=total+carro[i][2]
total=total-descuento1-descuento2

total_string=str(total)
total_lista=total_string.split(".")
decimal=total_lista[1]
largo=len(decimal)
decimal=int(decimal)
a=decimal//(10**(largo-1))
b=decimal%(10**(largo-1))
if (b//(10**(largo-2)))>=5:
    a=a+1
decimal=str(a)
total_lista[1]=decimal
total_string=".".join(total_lista)
total=float(total_string)

print(total)