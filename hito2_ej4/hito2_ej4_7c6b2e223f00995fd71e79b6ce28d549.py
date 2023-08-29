p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
lista_compras=[]
total=0
suma_p20=0
suma_p15=0
p20=0
p15=0


orden=input("Que desea hacer:")

if orden=="ver":
    for n in lista_compras:
        print(n[1])
        

elif orden=="checkout":
        
    for n in lista_compras:
        if n[0]==1 or n[0]==2 or n[0]==3:
            suma_p20+=n[2]
            p20+=1
        
        elif n[0]==4 or n[0]==5:
            suma_p15+=n[2]
            p15+=1
                
    total=suma_p20+suma_p15

    if p20!=0 and p15==0:
        total=total-(total*0.2)
    elif p20==0 and p15!=0:
        total=total-(total*0.15)
    elif p20!=0 and p15!=0:
        total=total-(total*0.15)
        total=total-(total*0.2)

    print(total)
            
                
                
                
else:
    producto=int(orden[0])
    cantidad=int(orden[2])
    if producto==1:
        i=1
        while i<=cantidad:
            lista_compras.append(p1)
            i+=1
            
    if producto==2:
        i=1
        while i<=cantidad:
            lista_compras.append(p2)
            i+=1
            
    if producto==3:
        i=1
        while i<=cantidad:
            lista_compras.append(p3)
            i+=1
            
    if producto==4:
        i=1
        while i<=cantidad:
            lista_compras.append(p4)
            i+=1
            
    if producto==5:
        i=1
        while i<=cantidad:
            lista_compras.append(p5)
            i+=1   