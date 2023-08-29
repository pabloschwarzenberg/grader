print("""
1: Juego Pokemon X para Nintendo 3DS, USD 33.77
2: Nintendo 3DS XL, USD 203
3: Juego Mario Kart 7 para Nintendo 3DS, USD 27.58
4: PlayStation 4, USD 348.00
5: FIFA 16, PlayStation 4, USD 51.19
""")

p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
carro = []
cuenta = 0
n=0
while n != True:
    n = input("Producto,cantidad: ")
    if n == "checkout":
        break
    if n == "ver":
        if c1 > 0:
            print(p1[1],c1)
        if c2 > 0:
            print(p2[1],c2)
        if c3 > 0:
            print(p3[1],c3)
        if c4 > 0:
            print(p4[1],c4)
        if c5 > 0:
            print(p5[1],c5)
    n = list(n)
    if n[0] == str(1):
        carro.append(p1)
        c1 += int(n[2])
    if n[0] == str(2):
        carro.append(p2)
        c2 += int(n[2])
    if n[0] == str(3):
        carro.append(p3)
        c3 += int(n[2])
    if n[0] == str(4):
        carro.append(p4)
        c4 += int(n[2])
    if n[0] == str(5):
        carro.append(p5)
        c5 += int(n[2])
cuenta = c1*float(p1[2]) + c2*float(p2[2]) + c3*float(p3[2]) + c4*float(p4[2]) + c5*float(p5[2])
if c1>0 and c2>0 and c3>0:
    cuenta = cuenta*0.8
if c4>0 and c5>0:
    cuenta = cuenta*0.75
print(round(cuenta,1))