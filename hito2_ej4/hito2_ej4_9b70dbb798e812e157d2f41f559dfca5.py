p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
compra=input("ingrese el producto y la cantidad que desea comprar(producto,cantidad): ")
lista=compra.split(",")
p=lista[0]
p=int(p)
c=lista[1]
c=int(c)
lista1=[p]
lista2=[c]
if p==p1[0]:
    a=c*p1[2]
elif p==p2[0]:
    a=c*p2[2]
elif p==p3[0]:
    a=c*p3[2]
elif p==p4[0]:
    a=c*p4[2]
elif p==p5[0]:
    a=c*p5[2]
h=0

while h==0:
  orden=input("que desea hacer?(agregar compra, ver, checkout): ")
  if orden=="agregar compra":
    compra=input("ingrese el producto y la cantidad que desea comprar(producto,cantidad): ")
    lista=compra.split(",")
    pf=lista[0]
    pf=int(pf)
    cf=lista[1]
    cf=int(cf)
    lista1.append(pf)
    lista2.append(cf)

  if orden=="ver":
     for x in range(0,len(lista1)):
      if lista1[x] in p1:
        print("de ",p1[1], "lleva ", lista2[x])
      if lista1[x] in p2:
        print("de ",p2[1], "lleva ",lista2[x])
      if lista1[x] in p3:
        print("de",p3[1],"lleva ",lista2[x])
      if lista1[x] in p4:
        print("de",p4[1], "lleva " ,lista2[x])
      if lista1[x] in p5:
        print("de " ,p5[1], "lleva" ,lista2[x])

    
  if orden=="checkout":
    a=0
    for x in range(0,len(lista1)):
      if lista1[x] in p1:
        a1=p1[2]*lista2[x]
        a=a+a1
        a=round(a,1)
      if lista1[x] in p2:
        a1=p2[2]*lista2[x]
        a=a+a1
        a=round(a,1)
      if lista1[x] in p3:
        a1=p3[2]*lista2[x]
        a=a+a1
        a=round(a,1)
        
      if lista1[x] in p4:
        a1=p4[2]*lista2[x]
        a=a+a1
        a=round(a,1)
  
      if lista1[x] in p5:
        a1=p5[2]*lista2[x]
        a=a+a1
        a=round(a,1)
    print(a)
    if 1 in lista1:
        if 2 in lista1:
            if 3 in lista1:
                print("por llevar el producto 1, 2 y 3, usted posee un descuento del 20%, su valor final queda en: ")
                b=a*0.8
                b=round(b,1)
                print(b)
    if 5 in lista1:
        if 4 in lista1:
            print("por llevar el producto 4 y 5, usted posee un descuento del 15%, su valor final queda en: ")
            b=a*0.85
            b=round(b,1)
            print(b)
             
    break
                  
                  