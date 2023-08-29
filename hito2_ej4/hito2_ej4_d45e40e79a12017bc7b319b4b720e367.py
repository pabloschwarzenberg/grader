total=0
productos=[]
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
while True:
    try:
    
        a=eval(input(" ingresa lo que quieras comprar:   "))
        b=a[0]
        productos.append()
        
        if a[0] ==1:
            pk=33.77
            c1=pk*a[1]
            total=total+c1
            print(total)
        
        
        if a[0] ==2:
            nt=203
            c1=nt*a[1]
            total=total+c1
            print(total)
            
        if a[0] ==3:
            mk=27.58
            c1=mk*a[1]
            total=total+c1
            print(total)
            
        if a[0] ==4:
            ps=348
            c1=ps*a[1]
            total=total+c1
            print(total)
            
        if a[0] ==5:
            ff=51.19
            c1=ff*a[1]
            total=total+c1
            print(total)
            
       
        print(total)
    except:
        print ("digita una opcion valida")
