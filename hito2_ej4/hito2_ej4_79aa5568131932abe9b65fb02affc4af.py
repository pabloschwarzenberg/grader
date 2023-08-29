p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro=[]
costo=0
pedido=input()
while pedido!="checkout":
    if pedido[0]=="1":
        costo=costo+(float(pedido[2])*float(p1[2]))
        carro.append(1)
        
    elif pedido[0]=="2":
        costo=costo+(float(pedido[2])*float(p2[2]))    
        carro.append(2)
        
    elif pedido[0]=="3":
        costo=costo+(float(pedido[2])*float(p3[2]))        
        carro.append(3)
        
    elif pedido[0]=="4":
        costo=costo+(float(pedido[2])*float(p4[2]))
        carro.append(4)
        
    elif pedido[0]=="5":
        costo=costo+(float(pedido[2])*float(p5[2]))
        carro.append(5)
        
    pedido=input()

if 1 in carro and 2 in carro and 3 in carro:
    if 4 in carro and 5 in carro:
        costo=costo*0.595
    else:
        costo=float(costo)*0.8
elif 4 in carro and 5 in carro:
        costo=costo*0.85
else:
    costo=costo


print(round(costo,1))