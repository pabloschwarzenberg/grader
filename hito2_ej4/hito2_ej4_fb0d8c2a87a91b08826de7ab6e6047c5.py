p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]
carrodecompras=""
costo=0
productos=""
c=1
while c==1:
    pc=input()
    x=pc[0]
    if x==str(p1[0]):
        carrodecompras = carrodecompras + p1[1]*(int(pc[2]))
        productos=productos + "p1"
        costo=costo + p1[2]*(int(pc[2]))
    elif x==str(p2[0]):
        carrodecompras = carrodecompras + p2[1]*(int(pc[2]))
        productos=productos + "p2"
        costo=costo + p2[2]*(int(pc[2]))
    elif x==str(p3[0]):
        carrodecompras = carrodecompras + p3[1]*(int(pc[2]))
        productos=productos + "p3"
        costo=costo + p3[2]*(int(pc[2]))
    elif x==str(p4[0]):
        carrodecompras = carrodecompras + p4[1]*(int(pc[2]))
        productos=productos + "p4"
        costo=costo + p4[2]*(int(pc[2]))
    elif x == str(p5[0]):
        carrodecompras = carrodecompras + p5[1] *(int(pc[2]))
        productos = productos + "p5"
        costo = costo + p5[2] *(int(pc[2]))
    else:
        c=2
a=productos.find("p1")
b=productos.find("p2")
c=productos.find("p3")
d=productos.find("p4")
e=productos.find("p5")
if a != -1 and b != -1 and c != -1 :
    costo = costo * 0.80
    costo = round(costo,1)
if d != -1 and e != -1 :
    costo = costo * 0.85
    costo = round(costo,1)
print(costo)


