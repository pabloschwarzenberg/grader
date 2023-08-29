p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro=[]
while 1!=2:
   a=input("Ingrese:")
   if a=="ver":
     print(carro)
   if a=="checkout":
     total=0
     
     i=0
     j=0
     k=0
     a=0
     b=0
     for sub in carro:
       if sub[0]==1:
         total+=p1[2]*sub[1]
         i=i+1
       if sub[0]==2:
         total+=p2[2]*sub[1]
         j=j+1
       if sub[0]==3:
         total+=p3[2]*sub[1]
         k=k+1
       if sub[0]==4:
         total+=p4[2]*sub[1]
         a=a+1
       if sub[0]==5:
         total+=p5[2]*sub[1]
         b=b+1
         
     if i>=1 and j>=1 and k>=1:
        total=total*0.8
     if a>=1 and b>=1:
        total=total*0.15
     print("Su total",str(total))
     break
   else:
     b=a.split(",")
     c=int(b[0])
     d=int(b[1])
     e=[c,d]
     carro.append(e)
       