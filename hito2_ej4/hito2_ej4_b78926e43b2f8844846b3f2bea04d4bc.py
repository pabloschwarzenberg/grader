p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
suma_total=0
compras=[]
n=""
print (p1,p2,p3,p4,p5)
v="VER"
k="CHECKOUT"
while n.upper() != k:
    n=input("¿Qué desea hacer? ")
    if n.upper()==v:
      print (compras) 
    elif len(n) ==3:
         if int(n[0])==1:
             i=0
             suma_total += 33.77 * int(n[2])
             print("se agregaron", n[2]," Pokemon X al carro")
             while i < int(n[2]):
                 compras.append("Pokemon X")
                 i+=1
         elif int(n[0])==2:
             i=0
             suma_total += 203 * int(n[2])
             print("se agregaron", n[2]," Nintendo XL al carro")
             while i < int(n[2]):
                 compras.append("Nintendo XL")
                 i+=1
         elif int(n[0])==3:
             i=0
             suma_total += 27.58 * int(n[2])
             print("se agregaron", n[2]," Mario Kart 7 al carro")
             while i < int(n[2]):
                 compras.append("Mario Kart 7")
                 i+=1
         elif int(n[0])==4:
             i=0
             suma_total += 348.00 *int( n[2] )
             print("se agregaron", n[2]," PlayStation 4 al carro")
             while i < int(n[2]):
                 compras.append("PlayStation 4")
                 i+=1
         elif int(n[0])==5:
             i=0
             suma_total += 51.19 *int(n[2])
             print("se agregaron", n[2]," FIFA 16 al carro")
             while i < int(n[2]):
                 compras.append("FIFA 16")
                 i+=1
    elif len(n)==4:
         q=int(n[2])*10 + int(n[3])
         if int(n[0])==1:
             i=0
             suma_total += 33.77 * q
             print("se agregaron", q," Pokemon X al carro")
             while i < q:
                 compras.append("Pokemon X")
                 i+=1
         elif int(n[0])==2:
             i=0
             suma_total += 203 * q
             print("se agregaron", q," Nintendo XL al carro")
             while i < q:
                 compras.append("Nintendo XL")
                 i+=1
         elif int(n[0])==3:
             i=0
             suma_total += 27.58 * q
             print("se agregaron", q," Mario Kart 7 al carro")
             while i < q:
                 compras.append("Mario Kart 7")
                 i+=1
         elif int(n[0])==4:
             i=0
             suma_total += 348.00 * q
             print("se agregaron", q," PlayStation 4 al carro")
             while i < q:
                 compras.append("PlayStation 4")
                 i+=1
         elif int(n[0])==5:
             i=0
             suma_total += 51.19 * q
             print("se agregaron", q," FIFA 16 al carro")
             while i < q:
                 compras.append("FIFA 16")
                 i+=1

t=compras.count("Pokemon X")
y= compras.count("Nintendo XL")
u=compras.count("Mario Kart 7")
d= compras.count("PlayStation 4")
f= compras.count("FIFA 16")
p=(33.77+203+27.58)
p2=(348.00+51.19)
if t <= y <=u or t<=u<=y :
            suma_total-= 0.2*p * t
elif  y<=u<=t or y<= t<= u:
            suma_total -= 0.2*p*y
elif u<=t<=y or u<=y<=t:
            suma_total -= 0.2 * p* u
if f<=d:
    suma_total-=0.15*f*p2
elif d<=f:
    suma_total-=0.15*d*p2
suma_total=round(suma_total, 1)
print(suma_total)
      