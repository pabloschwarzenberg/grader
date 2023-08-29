p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carrito=[]
while True:
      orden=input("")
      if orden=="ver":
         print(carrito)
      if orden=="checkout":
         plata=0
         s=0
         d=0
         u=0
         k=0
         l=0
         for n in carrito:
            if n[0]==1:
              plata+=p1[2]*n[1]
              s+=1
            if n[0]==2:
              plata+=p2[2]*n[1]
              d+=1
            if n[0]==3:
              plata+=p3[2]*n[1]
              u+=1
            if n[0]==4:
              plata+=p4[2]*n[1]
              k+=1
            if n[0]==5:
              plata+=p5[2]*n[1]
              l+=1
         if s>=1 and d>=1 and u>=1:
              plata=plata*0.8
         if k>=1 and l>=1:
              plata=plata*0.15
         print(str(plata))
         break
      else:
         l=orden.split(",")
         x=int(l[0])
         y=int(l[1])
         z=[x,y]
         carrito.append(z)
          
              
    