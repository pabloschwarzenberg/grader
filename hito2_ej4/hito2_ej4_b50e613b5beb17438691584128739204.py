p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos=[p1,p2,p3,p4,p5]

carro=[]
precio = []
i = 0
k = 0
while True:
    orden=str(input("Producto(1:5): "))
    producto = orden[0:1]
    cantidad = orden[2:]

    if orden == "ver":
        print(carro)

    elif orden == "checkout":
        #print(precio)
        if precio.count(1)>=1 in precio and precio.count(2)>=1 and precio.count(3)>=1:
            i = 0
            suma = 0
            total = 0
            while len(carro)>i:
                    b = carro[i][0][2]
                    #print(b)
                    d = float(b)
                    c = (carro[i][1])
                    #print(c)
                    f = float(c)
                    e = d * f
                    total = total + e
                    
                    i = i + 1   
            
            print(round(total*0.8,1))   

        elif precio.count(4)>=1 and precio.count(5)>=1:
            i = 0
            suma = 0
            total = 0
            while len(carro)>i:
                    b = carro[i][0][2]
                    #print(b)
                    d = float(b)
                    c = (carro[i][1])
                    #print(c)
                    f = float(c)
                    e = d * f
                    total = total + e
                    
                    i = i + 1    
            
            print(round(suma + total*0.85,1))   
        else:
            i = 0
            suma = 0
            while len(carro)>i:
                b = carro[i][0][2]
                    #print(b)
                d = float(b)
                c = (carro[i][1])
                #print(c)
                f = float(c)
                e = d * f
                suma = suma + e
                i = i + 1
            print(round(float(suma),1))
        break
            
            
    else:
        lista = []
        lista.append([producto,cantidad])

        for p in productos:
          if p[0]== int(lista[0][0]):
            compra=p
        item=[compra,lista[0][1]]
        carro.append(item)
        while True:
            a = carro[k][0][0]
            precio.append(a)
            k = k + 1
            break
        
            

        

#print(precio)    
#print(carro)

