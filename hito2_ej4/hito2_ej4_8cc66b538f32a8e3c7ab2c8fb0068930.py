p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos=[p1,p2,p3,p4,p5]
if __name__ == "__main__":
    total=0
    compra=[]
    while x==True:
    
    
        a=input("")
    
        compra.append(a)
    
    
        producto=a[0]
        cantidad=a[2]
        if a=="checkout":
        
            f=0
            while f<len(carro):
                total=total+carro[f][0][2]*carro[f][1]
                f=f+1
            x==False
            break
        elif a=="ver":
            print(carro)
        else:
            producto=int(a[0])
            cantidad=int(a[2])
    
            for p in productos:
                if p[0]==producto:
                    compra=p
                    break
        item=[compra,cantidad]
        carro.append(item)
    
    print(round(total,1))